from PIL import Image

import os

imageFolder = "/Users/Moco/Downloads/"
outputFolder = "/Users/Moco/Pictures/Compressed/"

if __name__ == '__main__':
    for filename in os.listdir(imageFolder):
        name, extension = os.path.splitext(imageFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            image = Image.open(imageFolder + filename)
            image.save(outputFolder + "compressed_" + filename, optimize=True, quality=65)
            os.remove(imageFolder + filename)
            print(name + ": " + str(os.path.getsize(name + extension)) + " bytes")
        
        if extension in [".mp3"]:
            musicFolder = "/Users/Moco/Music/"
            os.rename(imageFolder + filename, musicFolder + filename)
