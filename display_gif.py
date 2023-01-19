"""Displays an animated gif on a 64x64 RBG (not RGB!) LED Adafruit Matrix."""

import argparse
from pathlib import Path
import time

from PIL import Image, ImageSequence
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def get_frames(path):
    """Returns an iterable of gif frames."""
    frames = []
    with Image.open(path) as gif:
        for frame in ImageSequence.Iterator(gif):
            frame = frame.convert('RGB').resize((64,64)) # 64x64 matrix
            # GS: Re-arrange R, G, B for compatibility with Adafruit 64x64 matrix
            rgb = frame.split()
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            frame = Image.merge('RGB',(r,b,g)) # RBG
            frames.append(frame)
        return frames


def display_gif(path):
    """Displays gif frames on matrix."""
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    matrix = RGBMatrix(options=options)
    
    while True:
        for frame in get_frames(path):
            matrix.SetImage(frame)
            time.sleep(frame.info['duration']/1000)


def _get_parser():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description='Display gif on LED matrix.')
    parser.add_argument('gif_path',
                        nargs='?',
                        metavar='PATH_TO_GIF',
                        type=Path,
                        default=Path(__file__).parent / 'myGIF.gif',
                        help='the path to the gif file')
    
    return parser


if __name__ == '__main__':
    print('*********************************************\n'
          'display_gif script created by Heather Mahan.\n'
          'For more information, see documentation at\n'
          'https://github.com/poemusica/rpi-matrix-gif\n'
          '*********************************************')
    
    parser = _get_parser()
    args = parser.parse_args()
    parser.print_help()
    
    print('*********************************************'
          '\nThis script uses the rgbmatrix library by hzeller:\n'
          'https://github.com/hzeller/rpi-rgb-led-matrix')
    
    display_gif(args.gif_path)
