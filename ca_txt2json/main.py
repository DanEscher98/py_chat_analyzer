import os
import json
from ca_txt2json.cli import get_args
from ca_txt2json.digest import ParsedConversations


def main():
    args = get_args()
    in_file = args.FILE
    file_name = "output/" + os.path.basename(in_file).replace(".txt", "")

    with open(in_file, "r") as ifile:
        md_file = file_name + ".md"
        with open(md_file, "w") as ofile:
            conversations = ParsedConversations(ifile.read())
            for section in conversations.mdstr(args.name):
                ofile.write(section)

        if args.json:
            json_file = file_name + ".json"
            with open(json_file, "w") as json_file:
                json.dump(conversations.jsonobj(), json_file, sort_keys=True)

    print("File parsed sucessuflly")
