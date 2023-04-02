import os
import requests
import json
import time

import calendar as c
import wikipedia as wiki
import webbrowser as web
#CoreD 2 is an engine for LOGIC


#cache variables
c1=('')  
c2=('') 
c3=('') 
c4=('') 
c5=('') 
c6=('')
c7=(')')
def kelvic(c1):
    c2=(c1+273)
    print(c2)

def centif(c4):
    c3=((9/5)*c4+32)
    print(c3)

def build():
    os.system('cmd/c "build.bat"')

def crtmail(usr):
    response_API = requests.get('https://www.1secmail.com/api/v1/?action=getMessages&login='+usr+'&domain=1secmail.com')
    #print(response_API.status_code)
    data = response_API.text
    print('your temporary email:'+usr+'@1secmail.com')
    while True:
        time.sleep(5)
        print('mail received:'+data)
    
def fetchinfo():
    print("""
████████████████████████████████████████████████████████████████████████
█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░███████████░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░███████████░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░███░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████""")
    print('LOGIC:v1')
    print('Engine:CoreD 2')
    print('Developer:Blackhatdog')
    print('Version:Dev')

def calendaryy(yy):
    cl=(c.calendar(yy))
    print(cl)
def calendarmm(y2,mm):
    clm=(c.month(y2,mm))
    print(clm)


class webutils:
    def search(topic):
        data=(wiki.summary(topic))
        print(data)
    def openpage(url):
        web.open(url)




def dc_oct(c6):
    print(oct(c6))


def dc_hex(c7):
    print(hex(c7))
    

        
def clr_cache():
    c1=('')  
    c2=('') 
    c3=('') 
    c4=('') 
    c5=('') 
    c6=('') 
    c7=('') 


def shutdown():
    print('Thank you for using LOGIC')
    print('Shutting down.....')
    time.sleep(5)
    quit()


