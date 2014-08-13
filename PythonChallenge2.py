'''
Created on Aug 13, 2014

@author: miguel
'''
import urllib
if __name__ == '__main__':
    
    text = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
    text = text.read()
    text = str(text).split("<!--")[2]
    text = str(text).strip()
    dict = {}
    for key in text:
        if not key in dict:
            dict[key] = 1
        else:
            dict[key] += 1
    for key in dict:
        if dict[key] > 1:
            text = text.replace(key, "")
    print text[:-1]