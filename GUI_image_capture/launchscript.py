import os

#Upon starting Raspberry Pi, launhscript.sh will be called in the opening files. This shell script will then call this python command to start the focusstacking program

os.system('python live_stream.py --output output')
