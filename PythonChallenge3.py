'''
Created on 31/07/2014

@author: miguel
'''
import re
if __name__ == '__main__':
    
    mess = open("textChallenge3.txt")
    pageContents = mess.read()
    mess.close()
    exp = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
    pageContents = re.findall(exp, pageContents)
    print(pageContents)