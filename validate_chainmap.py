# .github/workflows/chainmap-validate.yml
name: ChainMap Strukturvalidierung

on:
  push:
    paths:
      - 'json/ChainMap_SyncModule.json'
  workflow_dispatch:

jobs:
  validate-structure:
    runs-on: ubuntu-latest
    steps:
      - name: Repository auschecken
        uses: actions/checkout@v3

      - name: Python-Umgebung vorbereiten
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Validierungsskript ausführen
        run: |
          mkdir -p scripts
          curl -o scripts/validate_chainmap.py https://raw.githubusercontent.com/virennasystems/virenna-core-dashboard/main/scripts/validate_chainmap.py
          python3 scripts/validate_chainmap.py json/ChainMap_SyncModule.json
