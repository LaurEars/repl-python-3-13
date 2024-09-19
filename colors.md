# Controlling colors
https://docs.python.org/3.13/using/cmdline.html#using-on-controlling-color

## Via Environment Variables
- `TERM=dumb` to disable entirely, explicitly set to "dumb" terminal
- `FORCE_COLOR` if set, overrides `TERM` (not in my testing)
- `NO_COLOR` if set, overrides `FORCE_COLOR`
- `PYTHON_COLORS` will set *only* python colors, not other tools

tl;dr: `PYTHON_COLORS` > `NO_COLOR` > `FORCE_COLOR` > `PYTHON_COLORS`

"set" here means anything other than empty string, including 0 and false

# Why did they do this?

Allows for piping result of commands into new process with color enabled
[`FORCE_COLOR`](https://force-color.org/) 
[`NO_COLOR`](https://no-color.org/)
