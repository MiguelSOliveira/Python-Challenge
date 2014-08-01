'''
Created on 31/07/2014

@author: miguel
'''

from zipfile import ZipFile
if __name__ == '__main__':
    
    nextFile = "90052"
    comments = []
    filename = '/home/miguel/Downloads/channel.zip'
    fileZip = ZipFile(filename)
    
    while 1:
        try:
            currentFile = open("/home/miguel/Downloads/channel/" + nextFile + ".txt")
            currentFileName = nextFile + ".txt"
            comments.append(fileZip.getinfo(currentFileName).comment)
            nextFile = currentFile.read()
            print(nextFile)
            nextFile = str(nextFile).split("Next nothing is ")[1]
        except:
            hugeTextImage = ("".join(str(i) for i in comments))
            hugeTextImage = str(hugeTextImage).replace("'b'", "").replace("b'", "")
            for i in range(0, len(hugeTextImage)):
                if hugeTextImage[i] == "\\" or hugeTextImage[i] == "n":
                    hugeTextImage = str(hugeTextImage).replace(hugeTextImage[i], "\n")
                else: pass
            print(hugeTextImage)
            break