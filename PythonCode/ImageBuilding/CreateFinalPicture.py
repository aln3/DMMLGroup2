from math import floor

from PIL import Image, ImageColor, ImageDraw
"""
This file opens the previous made pixel maps and creates one composite image of maps in a 5X2 formation.
These images were then taken and pasted over one and other in photoshop.
"""

x = 0
y = 0
im = Image.new('RGB', (240, 96))
for a in range(0, 10):
    image = Image.open('Top10pixels' + str(a) + '.png')
    im.paste(image, (x, y))
    x = x + 48
    if x == 240:
        x = 0
        y = y + 48
im.save('Top10.png')

x = 0
y = 0
im = Image.new('RGB', (240, 96))
for a in range(0, 10):
    image = Image.open('Top5pixels' + str(a) + '.png')
    im.paste(image, (x, y))
    x = x + 48
    if x == 240:
        x = 0
        y = y + 48
im.save('Top5.png')

x = 0
y = 0
im = Image.new('RGB', (240, 96))
for a in range(0, 10):
    image = Image.open('Top2pixels' + str(a) + '.png')
    im.paste(image, (x, y))
    x = x + 48
    if x == 240:
        x = 0
        y = y + 48
im.save('Top2.png')

x = 0
y = 0
im = Image.new('RGB', (240, 96))
for a in range(0, 10):
    image = Image.open('Top60pixels' + str(a) + '.png')
    im.paste(image, (x, y))
    x = x + 48
    if x == 240:
        x = 0
        y = y + 48
im.save('Top60.png')

x = 0
y = 0
im = Image.new('RGB', (240, 96))
for a in range(0, 10):
    image = Image.open('Top20pixels' + str(a) + '.png')
    im.paste(image, (x, y))
    x = x + 48
    if x == 240:
        x = 0
        y = y + 48
im.save('Top20.png')