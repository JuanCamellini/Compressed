from PIL import Image

import os

imageFolder = "/Users/Moco/Pictures/"
outputFolder = "/Users/Moco/Pictures/Compressed/"

if __name__ == '__main__':
    for filename in os.listdir(imageFolder):
        name, extension = os.path.splitext(imageFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            image = Image.open(imageFolder + filename)
            image.save(outputFolder + "compressed_" + filename, optimize=True, quality=65)

