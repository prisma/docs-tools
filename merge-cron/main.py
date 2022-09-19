import os
import platform
from time import sleep

hours = 24
system = platform.system() # Returns 'Windows' on Windows, 'Linux' on Linux, 'Darwin' on macOS, etc.

if system == 'Windows':
    os.system('init.bat')
elif system == 'Linux' or system == 'Darwin':
    os.system('init.sh')
else:
    print('Your system is not supported. Please run this script on Windows or Linux.')

os.system('cron.bat' if system == 'Windows' else 'cron.sh')

while True:
    sleep(hours*3600)
    os.system('cron.bat' if system == 'Windows' else 'cron.sh')
