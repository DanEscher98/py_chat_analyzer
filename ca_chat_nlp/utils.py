import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, Tuple, Iterator, List
import json
import re


def word_emoji_count(text: str) -> int:
    tokens = re.findall(r'\b\w+\b|:\w+:', text)
    return len(tokens)


def top_contributors(
        conversation: Dict[str, int], num: int = 1
        ) -> List[Tuple[str, int, float]]:
    total_wc = sum(conversation.values())
    authors: str = sorted(conversation, key=conversation.get)[num:]
    top_ac: List[Tuple[str, int, float]] = []

    for author in authors:
        percent = conversation[author] / total_wc
        top_ac.append((author, conversation[author], percent))

    return top_ac


def flatby_count(chat):
    """It """
    for (date, conversation) in chat.items():
        authors: Dict[str, int] = {}
        total_wc = 0
        for item in conversation:
            author = item['author']
            wc = word_emoji_count(item['msg'])
            authors[author] = authors.get(author, 0) + wc
            total_wc += wc


def digest(file: str):
    with open(file, "w") as f:
        contents: Dict[str, List[Dict[str, str]]] = json.load(f)
    


