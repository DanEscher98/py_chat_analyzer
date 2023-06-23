import re
import unidecode
import emoji
from urllib.parse import urlparse

url_regex = re.compile(r"(https?://\S+|www\.\S+|\S+\.\S+)")
chr_regex = re.compile('[' + re.escape("»{}'\"") + ']')


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


def urls2md(text: str) -> str:
    def convert_if_valid(url):
        parsed_url = urlparse(url)
        if all([parsed_url.scheme, domain := parsed_url.netloc]):
            if domain.startswith("www."):
                domain = domain[4:]
            if domain.endswith(".com"):
                domain = domain[:-4]
            return f"[{domain}]({url})"
        return url

    markdown_text = re.sub(url_regex,
                           lambda match: convert_if_valid(match.group(0)),
                           text)
    return markdown_text


def special2escaped(text: str) -> str:
    # return re.sub(chr_regex, lambda match: '\\' + match.group(), text)
    return re.sub(r"[\'\"]", "", text)


def utf2asciimd(message: str) -> str:
    url_mdify = urls2md(message)
    txt_demoji = emoji.demojize(url_mdify, delimiters=(" :", ": "))
    chr_asciify = unidecode.unidecode(txt_demoji, errors='replace')
    esc_special = special2escaped(chr_asciify)
    return esc_special
