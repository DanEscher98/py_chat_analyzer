from typing import TypeAlias, Dict, List
from dataclasses import dataclass

# {
#   "20250130": [
#     {
#       "author": "Yaretzi",
#       "msg": "Hola! Soy yare  :beaming_face_with_smiling_eyes:"
#     },
#     {
#       "author": "Danyiel Colin",
#       "msg": "Hi"
#     }
#   ]
# }

@dataclass
class Message:
    author: str
    msg: str

Chat: TypeAlias = Dict[str, List[Message]]

@dataclass
class StatsChatSlice:
    time_span: str
    participants: Dict[str, int]
    top_words: None | List[str]

# class DayChat:
#     def __init__(self, day_chat: )


# 1. Iterate through days
# 2. Agregate through weeks (top words)
# 3. Agregate through months (days)
# 4. Iterate through messages (participation)
