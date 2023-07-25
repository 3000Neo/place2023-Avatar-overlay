from PIL import Image
import os

def addImageToCanvas(imageFilePath, inputCanvas, xStart, yStart):
    input_image = Image.open(imageFilePath)
    input_pixel_map = input_image.load()
    src_width, src_height = input_image.size

    for x in range(src_width):
        for y in range(src_height):
            inputCanvas[(x+xStart+1500)*3 + 1, (y+yStart+1000)*3 + 1 ] = input_pixel_map[x,y]

    return

def addImageToCanvasCompact(imageFilePath, inputCanvas, xStart, yStart):
    input_image = Image.open(imageFilePath)
    input_pixel_map = input_image.load()
    src_width, src_height = input_image.size

    for x in range(src_width):
        for y in range(src_height):
            inputCanvas[(x+xStart+1500), (y+yStart+1000)] = input_pixel_map[x,y]

    return


redditWidth = 3000
redditHeight = 2000

outputImage = Image.new(mode="RGBA", size=(redditWidth*3, redditHeight*3), color=(0,0,0,0))
outputImageCompact = Image.new(mode="RGBA", size=(redditWidth, redditHeight), color=(0,0,0,0))

canvas = outputImage.load()
canvasCompact = outputImageCompact.load()

dirname = os.path.dirname(__file__)
imageFolder = os.path.join(dirname, '../../img/parts/png')

for file in os.listdir(imageFolder):
    filename = os.fsdecode(file)
    print("Checking File: " + filename)
    if(filename.endswith(".png")):
        tokens = filename.split(",")

        if(len(tokens) != 3):
            print("Tokens not matching: " + filename)
            continue


        try:

            xValue = int(tokens[0])
            yValue = int(tokens[1])

        except error:
            print("Tokens are not numbers: x=" + tokens[0] + " y=" + tokens[1])
            continue

        print("Adding to Canvas: " + filename)
        addImageToCanvas(os.path.join(imageFolder, filename), canvas, xValue, yValue)
        addImageToCanvasCompact(os.path.join(imageFolder, filename), canvasCompact, xValue, yValue)

outputImage.save(os.path.join(dirname, '../../img/overlay.png'))
outputImageCompact.save(os.path.join(dirname, '../../img/overlay_compact.png'))







