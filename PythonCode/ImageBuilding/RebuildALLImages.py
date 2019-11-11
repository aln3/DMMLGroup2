from PIL import Image, ImageColor
import csv

# This class will take the full data set and rebuild each of the 12000 images
contents = []
x = 0
y = 0
i = 0
z = 0
# change the file name to the full data set - if not in project directory use full path.
fileName = 'x_train_gr_smpl'
f = open("filename", "r")

with open('filename') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        im = Image.new('L', (48, 48))
        for i in row:
            value = int(i)
            im.putpixel((x, y), value)
            x = x + 1
            print(x)
            if x == 48:
                y = y+1
                print(y)
                x = 0
        im.save(str(z) + 'APixel.png')
        z = z + 1
        x = 0
        y = 0

