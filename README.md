# facewall
Creates a wall of faces

## How it works
The python script takes a _portraits_ directory as an argument.
It reads all the image files that are contained, resizes them to the dimension
_portrait_with_ x _portrait_height_ and pastes them one by one next to each other
onto a new _wall_name_ jpeg image. After every _columns_ images a new
row is starten on the wall.

## Usage
```
usage: facewall.py [-h]
                   [portraits] [columns] [portrait_width] [portrait_height]
                   [wall_name]

positional arguments:
  portraits        directory containing portrait images [default: 'portraits']
  columns          number of image columns on the wall [default: 16]
  portrait_width   width of a portrait [default: 500]
  portrait_height  height of a portrait [default: 500]
  wall_name        name of image wall[default: 'wall.jpg']

optional arguments:
  -h, --help       show this help message and exit
```
