'''
Created on 31/07/2014

@author: miguel
'''

import urllib.request
if __name__ == '__main__':
    
    page = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
    pageContents = page.read()
    nextNothing = (str(pageContents).split("is ")[1].split("'")[0])
    n = 0
    while (n < 400) :
        page = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nextNothing)
        pageContents = page.read()
        print(pageContents, n)
        if(n == 84):
            nextNothing = str(int(nextNothing) / 2)
            n+=1
            continue
        nextNothing = (str(pageContents).split("next nothing is ")[1].split("'")[0])
        n+=1
