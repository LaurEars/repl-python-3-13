# New Python REPL

Presentation notes from Los Angeles DevOps / SoCal Python combined meetup

[Los Angeles DevOps Meetup Link](https://www.meetup.com/ladevops/events/303272026)
[SoCal Python Meetup Link](https://www.meetup.com/socalpython/events/303403686/)
Sponsored by [Couchbase](https://www.couchbase.com/)

## REPL
- **R**ead
- **E**val
- **P**rint
- **L**oop

## Python 3.13 Release Notes
[A better interactive interpreter](https://docs.python.org/3.13/whatsnew/3.13.html#a-better-interactive-interpreter)

## People
### Based on PyPy interpreter by:
- Michael Hudson-Doyle
- Armin Rigo
### Contributions by:
- Pablo Galindo Salgado
- Łukasz Langa
- Lysandros Nikolaou
### Windows support from:
- Dino Viehland
- Anthony Shaw

## Requirements
- Unix-like: Python-based terminal requires `curses` and `readline`
- Windows
- Not WebAssembly or iOS

## Features

### Colors
![cat-color-glasses](images/cat-color-glasses.gif)

[Pretty colors!](colors.md)

### Updating functions to commands
- `help()` is now `help`
- `quit()` is now `quit`
- `exit()` is now `exit`

### Copy/paste

![SO copypaste keyboard](images/so-copy-paste.jpg)
[Stack Overflow copypaste keyboard](https://www.theverge.com/22761188/stack-overflow-the-key-copy-paste-review-price-release-date-keyboard)

## Demo
## Env Vars
- Disable everything by setting `PYTHON_BASIC_REPL` to 1

## Fun things
pydoc has its own http server
```shell
python -m pydoc -p 1234
```

## Notes
[Interactive mode](https://docs.python.org/3.13/tutorial/appendix.html#tut-interac)

[F1 to enter pydoc](https://docs.python.org/3.13/library/pydoc.html#module-pydoc)

modules, classes, functions and methods: extract doc from docstring stored in `__doc__`

F3 enters/exits paste mode

### podcast
[core.py podcast](https://podcasters.spotify.com/pod/show/corepy/episodes/Episode-10-The-Interactive-REPL-e2j788i/) form Pablo and Łukasz


### Other Env Vars

#### PYTHONBREAKPOINT
[PYTHONBREAKPOINT](https://docs.python.org/3.13/using/cmdline.html#envvar-PYTHONBREAKPOINT)

[Example .zshrc file](https://github.com/LaurEars/dotfiles/blob/54b746810b808a4576e523cba17b07dea2b8a503/.zshrc#L25)
```shell
export PYTHONBREAKPOINT=ipdb.set_trace
```

[PYTHON_BASIC_REPL](https://docs.python.org/3.13/using/cmdline.html#envvar-PYTHON_BASIC_REPL)
If set to 1, use a REPL that does not require `curses` and `readline`

[PYTHONMALLOCSTATS](https://docs.python.org/3.13/using/cmdline.html#envvar-PYTHONMALLOCSTATS)
Set to anything to enable
