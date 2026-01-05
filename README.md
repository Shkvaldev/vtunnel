# Vtunnel
> Simple proxy that uses white-listed services (like VK or MAX) to bypass censorship

## Setting up

First of all, you must generate `words.txt`, `mappings.json` and `dialogs.json` and sync
them with client and server. This is needed because project uses linguistic stego.

0. Install deps from `requirements.txt`
1. Generate files using `generate_files.py` and change some dialogs in `dialogs.json`
2. Fill in `config.json`
3. Copy generated files to both client and server and execute `main.py`

## TODO
- `Dialogs` implementation
- `Message Builder` implementation
- `MaxProvider` implementation
- `OKProvider` implementation
