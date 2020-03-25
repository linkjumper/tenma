# tenma

Easy to use control script for tenma power supply. Tested on TN72-2540.

## Install

```bash
> pip install -r requirements.txt
``` 

Add tenma.py to your PATH's variable by e.g creating a symlink for tenma.py
to your local ~/bin folder. 

## Usage
Assume you want the power supply to be 12V with 0.5A maximum.

```bash
> tenma.py -v 12 -c 0.5
# Terminate the script by pressing CTRL+C
```

