# Template project for KOOK Bot

## Brief

This project is for easily create a kook bot with a simple framework and can be build to a single windows executable
file.

Project use [khl.py](https://github.com/TWT233/khl.py) for communication with kook, and
use [pyinstaller](https://github.com/pyinstaller/pyinstaller) for executable file building.

## Environment Prepare

```shell
pip install khl.py
pip install pyinstaller
```

Create a `config.json` file in project root, content refers to `config.example.json`.

Run `python main.py` to start your bot.

## Build Dist

```shell
pyinstaller ./main.spec --clean
```

The final artifact will appear in dist/*