from DrawSVG.drawSVG import SVG
import shutil

allBackgroundColors = list(['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'white'])
size = 200
layerStep = 50 #Must be devidable by width and height
folder = '/SVGs/'


def createBackground(xxx):
    layerSize = 200
    mySVG = SVG({'width':size, 'height':size})
    mySVG.addChildElement('rect', {'x':0, 'y':0, 'width':layerSize, 'height':layerSize, 'fill': xxx})
    mySVG.write('background'+str(xxx.title())+'.svg')

def createAllLayersSeparately():
    layerSize = 200
    for layer in range(int(size/layerStep)):
        for color in allBackgroundColors:
            currLayerSize = layerSize-(layerStep*layer)
            layerPos = (size/2)-((currLayerSize)/2)
            mySVG = SVG({'width':size, 'height':size})
            mySVG.addChildElement('rect', {'x':layerPos-5, 'y':layerPos-5, 'width':currLayerSize+10, 'height':currLayerSize+10, 'fill': 'black'})
            mySVG.addChildElement('rect', {'x':layerPos, 'y':layerPos, 'width':currLayerSize, 'height':currLayerSize, 'fill': color})
            currFileName = str(layer)+str(color.title())+'.svg'
            currFilePath = folder+currFileName
            mySVG.write(currFileName)
            print(currFileName+' created')
            shutil.move(currFileName, currFilePath)
            print(currFileName+' moved to '+currFilePath)

if __name__ == '__main__':
    #for color in allBackgroundColors:
    #    createBackground(color)
    createAllLayersSeparately()