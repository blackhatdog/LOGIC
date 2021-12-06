from pyfiglet import Figlet
import os
import calendar
import pycalc
import core
from core import *

    
    



f = Figlet()
print(f.renderText('>_Shell'))
while True:
    prompt=(input('@System#>'))
    if prompt == 'cmd':
        os.system('cmd/c ')
    else:
        exec(prompt)
    
         
           
        
