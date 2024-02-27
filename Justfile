set shell := ["bash", "-c"]

convert FILE NAME:
  @NAME=$(basename {{FILE}} .txt);\
  poetry run watxt2json data/$NAME.txt --name "{{NAME}}" --json;\
  echo "Done: txt -> (json, md)";\

pdf FILE:
  @NAME=$(basename {{FILE}} .md);\
  pandoc output/$NAME.md -o output/$NAME.pdf --standalone;\
  echo "Done: md -> pdf";\
  cp output/$NAME.pdf ~/Downloads;\
  evince -p 1 output/$NAME.pdf
