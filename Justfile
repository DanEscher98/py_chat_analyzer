set shell := ["bash", "-c"]

convert FILE NAME:
  @NAME=$(basename {{FILE}} .txt);\
  poetry run watxt2json data/$NAME.txt --name {{NAME}};\
  echo "Done: txt -> md";\
  just pandoc $NAME;\
  echo "Done: md -> pdf"

pandoc FILE:
  @NAME=$(basename {{FILE}} .md);\
  pandoc output/$NAME.md -o output/$NAME.pdf --standalone
