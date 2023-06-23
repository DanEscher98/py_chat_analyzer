set shell := ["bash", "-c"]

convert FILE:
  @NAME=$(basename {{FILE}} .txt);\
  poetry run watxt2json data/$NAME.txt;\
  echo "Done: txt -> md";\
  just pandoc $NAME;\
  echo "Done: md -> pdf"

pandoc FILE:
  @NAME=$(basename {{FILE}} .md);\
  pandoc output/$NAME.md -o output/$NAME.pdf --metadata-file=pandoc_cfg.yaml --toc --standalone
