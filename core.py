import os
import requests
import json
import time
from pyfiglet import Figlet
import calendar as c
import wikipedia as wiki
import webbrowser as web
#CoreD I4 is an engine for shellsys


def kelvic(c):
    r1=(c+273)
    print(r1)

def centif(f):
    r2=((9/5)*f+32)
    print(r2)

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
    op1 = Figlet()
    print(op1.renderText('CoreD I4'))
    print('Shell Version:v1')
    print('Engine:CoreD I4')
    print('Developer:Blackhatdog')
    print('Version:Dev')

def calendaryy(yy):
    cl=(c.calendar(yy))
    print(cl)
def calendarmm(y2,mm):
    clm=(c.month(y2,mm))
    print(clm)


class onlineutilities:
    def search(topic):
        data=(wiki.summary(topic))
        print(data)
    def openpage(url):
        web.open(url)

    
        
        


