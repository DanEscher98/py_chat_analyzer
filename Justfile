set shell := ["bash", "-c"]

convert FILE:
  @NAME=$(basename {{FILE}} .txt);\
  uv run -m ca_txt2json.main data/$NAME.txt --json; \
  cat output/$NAME.json | jq > output/fmt_$NAME.json
  echo "Done: txt -> (json, md)";\

pdf FILE:
  @NAME=$(basename {{FILE}} .md);\
  pandoc output/$NAME.md -o output/$NAME.pdf --standalone -V geometry:margin=2cm;\
  echo "Done: md -> pdf";\
  cp output/$NAME.pdf ~/Downloads;\
  evince -p 1 output/$NAME.pdf

install:
  uv sync --all-groups

format:
  uv run ruff check .

test:
  uv run pytest -v
  #uv run pytest --cov=
