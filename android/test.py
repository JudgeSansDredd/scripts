import pathlib

import numpy
from PIL import Image
from ppadb.client import Client as ADBClient

DIR_PATH = str(pathlib.Path(__file__).parent.resolve())
IMAGE_PATH = f'{DIR_PATH}/screencap.png'
ADB_PARAMS = {
    'port': 5037,
    'host': '127.0.0.1'
}

def takeScreenshot():
    adbClient = ADBClient(**ADB_PARAMS)
    devices = adbClient.devices()
    if len(devices) == 0:
        print("No devices connected!")
        exit()

    with open(IMAGE_PATH, 'wb') as fh:
        fh.write(devices[0].screencap())

def getTwoDimensionPixels():
    image = Image.open(IMAGE_PATH)
    return numpy.array(image, dtype=numpy.uint8)

def main():
    takeScreenshot()
    twoDimPixels = getTwoDimensionPixels()

if __name__ == '__main__':
    main()
