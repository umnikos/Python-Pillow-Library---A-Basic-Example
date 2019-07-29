#!/usr/bin/python3

from PIL import Image

size = (500,433)
im = Image.new("1",size, 0)
px = im.load()

def triangle(xy, fill=1, depth=5):
    if depth == 0:
        px[xy[0],xy[1]] = fill
        return
    triangle(((3*xy[0]+xy[2])//4, 
               xy[1],
               (xy[0]+3*xy[2])//4,
               (xy[1]+xy[3])//2), 
               fill,
               depth-1)
    triangle((xy[0],
              (xy[1]+xy[3])//2, 
              (xy[0]+xy[2])//2,
              xy[3]),
              fill,
              depth-1)
    triangle(((xy[0]+xy[2])//2,
              (xy[1]+xy[3])//2,
              xy[2],
              xy[3]),
              fill,
              depth-1)

triangle((0,0)+size, depth=10)
im.show()
im.save("output.png","PNG")

