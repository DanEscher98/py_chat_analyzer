import unidecode
import re
import textwrap
from typing import List, Iterator, Dict
from ca_txt2json.format import utf2asciimd, pandoc_yaml, Date


class Message:

    def __init__(self, sender: str):
        self.message: List[str] = []
        self.sender = unidecode.unidecode(sender, errors='ignore').strip()

    def append(self, message: str):
        self.message.append(utf2asciimd(message))

    def __str__(self):
        message = "-- {}: {}".format(self.sender, ". ".join(self.message))
        return textwrap.fill(message, width=100,
                             break_long_words=False,
                             break_on_hyphens=False)


class Conversation:
    """A dialog on the span of a single day"""

    def __init__(self, date: str, contents):
        self.date: Date = Date(date)
        self.contents: List[Message] = contents

    def __str__(self):
        return "## {}\n\n{}\n\n{}\n\n\n".format(
                self.date.human_readable(),
                "\n\n".join(map(str, self.contents)),
                "".join(["-"] * 80))


class ParsedConversations:
    def __init__(self, file):
        self.conversations: List[Conversation] = parse_chat(file)

    def jsonobj(self) -> Dict[int, List[Dict[str, str]]]:
        data: Dict[int, List[Dict[str, str]]] = {}
        for convo in self.conversations:
            date = convo.date.id()
            conversation = []
            for msg in convo.contents:
                conversation.append({
                    "author": msg.sender,
                    "msg": " ".join(msg.message)
                })
            data[date] = conversation

        return data

    def mdstr(self, name="a Person") -> Iterator[str]:
        date_start = self.conversations[0].date.simple()
        date_end = self.conversations[-1].date.simple()
        yield pandoc_yaml(f"A conversation with {name}",
                          f"From {date_start} to {date_end}")
        for convo in self.conversations:
            yield str(convo)


def parse_chat(text: str) -> List[Conversation]:
    """Generates a list of `Conversation`s. from an txt WhatsApp file"""

    pattern = r"(\d+/\d+/\d+), (\d+:\d+\s*[APM]*) - ([^:\n]+): ([^\n]*)"
    matched_msg = iter(re.findall(pattern, text, re.MULTILINE | re.DOTALL))

    curr_date, _, curr_sender, message = next(matched_msg)
    curr_msg = Message(curr_sender)
    curr_msg.append(message)
    daily_convo: List[Message] = []
    convo_history: List[Conversation] = []

    for date, _, sender, message in matched_msg:
        # Date has changed, so new Conversation and Message
        if date != curr_date:
            daily_convo.append(curr_msg)
            convo_history.append(Conversation(curr_date, daily_convo))
            curr_date = date
            daily_convo = []
            curr_msg = Message(curr_sender)  # shadowing

        # Sender has changed, so new Message
        if sender != curr_sender:
            daily_convo.append(curr_msg)
            curr_msg = Message(curr_sender := sender)  # shadowing

        curr_msg.append(message)

    daily_convo.append(curr_msg)
    convo_history.append(Conversation(curr_date, daily_convo))

    return convo_history
