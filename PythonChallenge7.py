'''
Created on 01/08/2014

@author: miguel
'''

import Image
if __name__ == '__main__':
    
    image = Image.open("oxygen.png")
    image.show()
    width, height = image.size
    y = image.size[1] / 2
    print "".join(chr(image.getpixel((x, y))[0]) for x in range(0, width, 7))
    a, b, c, d, e, f, g, h, i = 105, 110, 116, 101, 103, 114, 105, 116, 121
    print chr(a),
    print chr(b),
    print chr(c),
    print chr(d),
    print chr(e),
    print chr(f),
    print chr(g),
    print chr(h),
    print chr(i)

