'''
Created on Aug 13, 2014

@author: miguel
'''

if __name__ == '__main__':
    
    sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    sentence = "map"
    newSentence = ""
    for i in sentence:
        if i == " ":
            newSentence += " "
            continue
        elif i == 'z':
            newSentence += "b"
            continue
        elif i == 'y':
            newSentence += "a"
            continue
        elif i == '.':
            newSentence += "."
            continue
        newSentence += (chr(ord(i)+2))
    print newSentence