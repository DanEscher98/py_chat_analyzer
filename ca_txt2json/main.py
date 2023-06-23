import os
from ca_txt2json.cli import get_args
from ca_txt2json.digest import parse_chat
from ca_txt2json.format import pandoc_yaml


def main():
    args = get_args()
    input_file = args.FILE
    output_file = "output/" + os.path.basename(
            input_file.replace(".txt", ".md"))
    with open(input_file, "r") as ifile:
        with open(output_file, "w") as ofile:
            conversations = parse_chat(ifile.read())
            date_start = conversations[0].date
            date_end = conversations[-1].date
            print(f"# Days: {len(conversations)}")
            ofile.write(pandoc_yaml("A conversation with Esteban Argumedo",
                                    f"From {date_start} to {date_end}"))
            for convo in conversations:
                ofile.write(str(convo))
        with open(output_file, "r") as ofile:
            print(f"Total lines: {len(ofile.readlines())}")

    print("Program sucessuflly finished")
