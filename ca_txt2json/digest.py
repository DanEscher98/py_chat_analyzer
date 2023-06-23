import unidecode
import re
import textwrap
from typing import List
from ca_txt2json.format import utf2asciimd


class Message:
    def __init__(self, sender: str):
        self.sender = unidecode.unidecode(sender, errors='ignore').strip()
        self.message: List[str] = []

    def append(self, message: str):
        self.message.append(utf2asciimd(message))

    def __str__(self):
        message = "-- {}: {}".format(self.sender, ". ".join(self.message))
        return textwrap.fill(message, width=100,
                             break_long_words=False,
                             break_on_hyphens=False)


class Conversation:
    def __init__(self, date: str, contents: List[Message]):
        self.date = date
        self.contents = contents

    def __str__(self):
        return "## {}\n\n{}\n\n{}\n\n\n".format(
                self.date,
                "\n\n".join(map(str, self.contents)),
                "".join(["-"] * 80))


def parse_chat(text: str) -> List[Conversation]:
    pattern = r"(\d+/\d+/\d+), (\d+:\d+\s*[APM]*) - ([^:\n]+): ([^\n]*)"
    matches = iter(re.findall(pattern, text, re.MULTILINE | re.DOTALL))

    curr_date, curr_sender = "0/0/0", "nobody"
    curr_msg = Message(curr_sender)
    daily_convo: List[Message] = []
    ret: List[Conversation] = []

    for date, _, sender, message in matches:
        if date != curr_date:
            daily_convo.append(curr_msg)
            ret.append(Conversation(curr_date, daily_convo))
            curr_date = date
            daily_convo = []
            curr_msg = Message(curr_sender)

        if sender != curr_sender:
            daily_convo.append(curr_msg)
            curr_msg = Message(curr_sender := sender)

        curr_msg.append(message)

    daily_convo.append(curr_msg)
    ret.append(Conversation(curr_date, daily_convo))
    del ret[1].contents[0]  # remove the nobody msg
    del ret[0]              # remove the 0/0/0 date
    return ret
