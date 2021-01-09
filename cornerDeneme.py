from PIL import Image, ImageDraw
#Execution body
def add_corners (im, rad):
    circle = Image.new ('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw (circle)
    draw.ellipse ((0, 0, rad * 2, rad * 2), fill = 255)
    alpha = Image.new ('L', im.size, 255)
    w, h = im.size
    alpha.paste (circle.crop ((0, 0, rad, rad)), (0, 0))
    alpha.paste (circle.crop ((0, rad, rad, rad * 2)), (0, h-rad))
    alpha.paste (circle.crop ((rad, 0, rad * 2, rad)), (w-rad, 0))
    alpha.paste (circle.crop ((rad, rad, rad * 2, rad * 2)), (w-rad, h-rad))
    im.putalpha (alpha)
    return im
im = Image.open ('/Users/anilyavuz6176gmail.com/Desktop/ss/tests/test3.png') # Set image
im = add_corners (im, 100) #Execute the rounded method with arguments
im.save ('/Users/anilyavuz6176gmail.com/Desktop/ss/tests/test30.png') # After execution