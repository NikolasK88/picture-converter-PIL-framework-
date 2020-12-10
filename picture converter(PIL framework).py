import requests
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps
import numpy as np





def craete_bg():
    img = Image.new('RGB', (400, 400), color='white')
    img.save('bg2.1.jpg')

def get_web_image (url):
    img_data = requests.get(url).content
    with open('pic3.jpg', 'wb') as handler:
        handler.write(img_data)


def paste_image (source, destination, x, y, omit_color="None"):
    fg = Image.open(source)
    bg = Image.open(f'{destination}{y}.{x}.jpg')
    newsize = (400, 400)
    bg = bg.resize(newsize)
    fg = fg.resize(newsize)

    if omit_color == 'transparent':
        fg = Image.open(source).convert('RGBA')
        newsize = (400, 400)
        bg = bg.resize(newsize)
        fg = fg.resize(newsize)
        w, h = fg.width, fg.height
        for i in range(h):
            for k in range(w):
                r, g, b, a = fg.getpixel((i, k))
                print(a)
                if a > 128:
                    bg.putpixel((i, k), (r, g, b))
        newsize = (400, 400)
        bg = bg.resize(newsize)
        bg.save(f'{destination}{y}.{x}.jpg')
    else:
        new_pixels = []
        for i in range(0, 400):
            pixel_row = []
            for k in range(0, 400):
                hor = k
                vert = i
                cordinate = hor, vert
                pixel_row.append(fg.getpixel(cordinate))
            new_pixels.append(pixel_row)
        array = np.array(new_pixels, dtype=np.uint8)
        new_pixels = Image.fromarray(array)
        new_pixels.save(f'{destination}{y}.{x}.jpg')

    part1 = Image.open('bg1.1.jpg')
    part2 = Image.open('bg1.2.jpg')
    part3 = Image.open('bg1.3.jpg')
    part4 = Image.open('bg2.1.jpg')
    part5 = Image.open('bg2.2.jpg')
    part6 = Image.open('bg2.3.jpg')

    new_pixels1 = []
    new_pixels2 = []
    new_pixels3 = []
    new_pixels4 = []
    new_pixels5 = []
    new_pixels6 = []

    final_list1 = []
    final_list2 = []

    for i in range(0, 400):
        pixel_row1 = []
        pixel_row2 = []
        pixel_row3 = []
        pixel_row4 = []
        pixel_row5 = []
        pixel_row6 = []
        for k in range(0, 400):
            hor = k
            vert = i
            cordinate = hor, vert
            pixel_row1.append(part1.getpixel(cordinate))
            pixel_row2.append(part2.getpixel(cordinate))
            pixel_row3.append(part3.getpixel(cordinate))
            pixel_row4.append(part4.getpixel(cordinate))
            pixel_row5.append(part5.getpixel(cordinate))
            pixel_row6.append(part6.getpixel(cordinate))
        new_pixels1.append(pixel_row1)
        new_pixels2.append(pixel_row2)
        new_pixels3.append(pixel_row3)
        new_pixels4.append(pixel_row4)
        new_pixels5.append(pixel_row5)
        new_pixels6.append(pixel_row6)

    for pixel in range(len(new_pixels1)):
        new_pixels1_123 = new_pixels1[pixel] + new_pixels2[pixel] + new_pixels3[pixel]
        final_list1.append(new_pixels1_123)

    for pixel in range(len(new_pixels4)):
        new_pixels2_123= new_pixels4[pixel] + new_pixels5[pixel] + new_pixels6[pixel]
        final_list2.append(new_pixels2_123)

    final_list = final_list1 + final_list2

    array = np.array(final_list, dtype=np.uint8)
    final_picture = Image.fromarray(array)
    final_picture.save('collage.jpg')















def invert_colors(img): #for Color Manipulation
    im = Image.open(img)
    inverted = PIL.ImageOps.invert(im)
    inverted.save('picture3_inverted.jpg')

def flip(img, axis): # axis is horizontal or vertical      for Pixel position
    im = Image.open(img)
    if axis == 'horizontal':
        result = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif axis == 'vertical':
        result = im.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        print('wrong axis, try again!')
    result.save('flipped.jpg')

def rotate(img):     # for Other functions
    im = Image.open(img)
    im = im.rotate(45)
    im.save('rotated.jpg')


def put_text(img, doc):
    im = Image.open(img)
    font = ImageFont.truetype("arial.ttf", 100)
    text = open(doc, "r").read()
    draw = ImageDraw.Draw(im)
    draw.text((300, 300), text, (0, 0, 255), font)
    im.save('collage_with_text.jpg')




#my_img_object = get_web_image ('https://baseballtips.com/wp-content/uploads/2012/10/6fullmound_1-400x400.jpg')


#paste_image('pic3.jpg',f'bg', 3,2, '')


#put_text('collage.jpg', 'data.txt')
#rotate('pic1.jpg')   #ok
#flip('pic1.jpg', 'horizontal') #ok
#invert_colors('pic3.png')

