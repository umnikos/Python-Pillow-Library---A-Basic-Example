#!/usr/bin/python3

from PIL import Image

size = (512, 443)  # the size of the final image
# create a new black and white image
im = Image.new(
    "1", size, 0
)
px = im.load()  # create a pixel access object


# takes a 4-tuple range of where to draw the sierpinski triangle
def triangle(xy, fill=1, depth=5):
    # if recursion is over, fill the top left pixel
    if depth == 0:
        px[xy[0], xy[1]] = fill
        return
    # otherwise, draw 3 smaller sierpinski triangles
    triangle(
        (
            (3 * xy[0] + xy[2]) // 4,
            xy[1],
            (xy[0] + 3 * xy[2]) // 4,
            (xy[1] + xy[3]) // 2,
        ),
        fill,
        depth - 1,
    )
    triangle(
        (
            xy[0],
            (xy[1] + xy[3]) // 2,
            (xy[0] + xy[2]) // 2,
            xy[3],
        ),
        fill,
        depth - 1,
    )
    triangle(
        (
            (xy[0] + xy[2]) // 2,
            (xy[1] + xy[3]) // 2,
            xy[2],
            xy[3],
        ),
        fill,
        depth - 1,
    )

# draw the triangle (smaller depths results in a dotty output)
triangle(
    (0, 0, size[0], size[1]), depth=10
)
im.save("output.png", "PNG")  # save the image
im.show()  # open the image
