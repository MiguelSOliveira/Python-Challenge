'''
Created on 31/07/2014

@author: miguel
'''

import urllib.request, pickle
if __name__ == '__main__':
    
    page = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    pagePickled = pickle.load(page)
    for tuples in pagePickled:
        print("".join(i[0]*i[1] for i in tuples))
