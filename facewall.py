#!/usr/bin/env python3

import argparse
import logging
from os import listdir
from os.path import isfile, join

from PIL import Image


def create_wall(portraits_dir: str, columns: int, portrait_width: int, portrait_height: int, wall_name: str):
    logging.info("Reading images from directory '{}'...\n".format(portraits_dir))
    dir_entries = [join(portraits_dir, f) for f in listdir(portraits_dir)]
    files = [f for f in dir_entries if isfile(f)]
    files.sort()
    wall_width = len(files) * portrait_width if len(files) < columns else columns * portrait_width
    wall_height = (len(files) // columns + 1) * portrait_height
    wall = Image.new('RGB', (wall_width, wall_height))
    for idx, file in enumerate(files):
        image = Image.open(file)
        resized_img = image.resize((portrait_width, portrait_height))
        wall.paste(resized_img, (idx % columns * portrait_width, (idx // columns) * portrait_height))
    logging.info("Saving '{}'...\n".format(wall_name))
    wall.save(wall_name, "JPEG", quality=80, optimize=True, progressive=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("portraits", nargs='?', type=str, default="portraits",
                        help="directory containing portrait images [default: 'portraits']")
    parser.add_argument("columns", nargs='?', type=int, default=16,
                        help="number of image columns on the wall [default: 16]")
    parser.add_argument("portrait_width", nargs='?', type=int, default=500, help="width of a portrait [default: 500]")
    parser.add_argument("portrait_height", nargs='?', type=int, default=500, help="height of a portrait [default: 500]")
    parser.add_argument("wall_name", nargs='?', type=str, default="wall.jpg", help="name of image wall[default: 'wall.jpg']")
    args = parser.parse_args()
    create_wall(portraits_dir=args.portraits, columns=args.columns, portrait_width=args.portrait_width,
                portrait_height=args.portrait_height, wall_name=args.wall_name)


if __name__ == '__main__':
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    main()
