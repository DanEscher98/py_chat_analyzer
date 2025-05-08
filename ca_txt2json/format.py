import re
import unidecode
import datetime
import emoji
from urllib.parse import urlparse

url_regex = re.compile(r"(https?://\S+|www\.\S+|\S+\.\S+)")
chr_regex = re.compile('[' + re.escape("»{}'\"") + ']')

class Date:
    def __init__(self, date: str):
        #self.date = datetime.datetime.strptime(date, "%m/%d/%y")
        self.date = datetime.datetime.strptime(date, "%d/%m/%y")

    def simple(self) -> str:
        return self.date.strftime("%d/%m/%Y")

    def human_readable(self) -> str:
        return self.date.strftime("%A %d/%B/%Y")

    def id(self) -> int:
        return int(self.date.strftime("%Y%m%d"))


def pandoc_yaml(convo_name, date_range) -> str:
    return f"""---
colorlinks: true
nameInLink: true
linkcolor: blue
date: \\today
papersize: a4
toc: true
toc-title: {"The index"}
title: {convo_name}
subtitle: {date_range}
header-includes:
    - \\usepackage[utf8]{"{inputenc}"}
---\n\n"""


def url2md(text: str) -> str:
    """Finds all urls and replace them with markdown format for links"""
    def convert_if_valid(url):
        parsed_url = urlparse(url)
        if all([parsed_url.scheme, domain := parsed_url.netloc]):
            if domain.startswith("www."):
                domain = domain[4:]
            if domain.endswith(".com"):
                domain = domain[:-4]
            return f"[{domain}]({url})"
        return url

    mdurl_text = re.sub(url_regex,
                        lambda match: convert_if_valid(match.group(0)),
                        text)
    return mdurl_text


def special2latex(text: str) -> str:
    """Converts or removes special characters in order to produce
    compilable Latex strings"""
    # return re.sub(chr_regex, lambda match: '\\' + match.group(), text)
    return re.sub(r"[\'\"]", "", text)


def utf2asciimd(message: str) -> str:
    """Applies multiple filters to convert a UTF string into plain ascii
    Markdown format.
    1. Converts `url`s to markdown syntax
    2. Replace emojis with its textual form
    3. Remove any left character non ascii
    4. Handles special characters"""
    url_mdify = url2md(message)
    txt_demoji = emoji.demojize(url_mdify, delimiters=(" :", ": "))

    preserved = txt_demoji \
        .replace("ñ", "<<N_TILDE_LOWER>>") \
        .replace("Ñ", "<<N_TILDE_UPPER>>")
    
    chr_asciify = unidecode.unidecode(preserved, errors='replace')
    
    latexified = chr_asciify \
        .replace("<<N_TILDE_LOWER>>", r"ñ" ) \
        .replace("<<N_TILDE_UPPER>>", r"Ñ")
    
    esc_special = special2latex(latexified)
    return esc_special
