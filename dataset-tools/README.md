# dataset-tools

This is a package of tools for quickly normalizing image datasets to be ready for a Generative Adversarial Network.
On normalizing image datasets—many utilizing this set of scripts—on [my YouTube page](https://www.youtube.com/playlist?list=PLWuCzxqIpJs9v81cWpRC7nm94eTMtohHq).

## Installation

```
git clone https://github.com/dvschultz/dataset-tools.git
cd dataset-tools
pipenv shell
pip install -r requirements.txt
```

## Basic Usage

```
python dataset-tools.py --input_folder path/to/input/ --output_folder path/to/output/
python dataset-tools.py --input_folder /Users/khaledkaddal/Desktop/resense/Gearloose/DataSets/iris/2_ouptut1024 --output_folder /Users/khaledkaddal/Desktop/resense/Gearloose/DataSets/iris/ --process_type square --border_type solid --border_color 0,0,0
```

## All Options

### dataset_tools.py

- `--verbose`: Print progress to console.
- `--input_folder`: Directory path to the inputs folder. _Default_: `./input/`
- `--output_folder`: Directory path to the outputs folder. _Default_: `./output/`
- `--process_type`: Process to use. _Options_: `resize`,`square`,`crop`,`crop_to_square`,`canny`,`canny-pix2pix`,`scale`,`crop_square_patch`,`many_squares` _Default_: `resize`
- `--blur_type`: Blur process to use. Use with `--process_type canny`. _Options_: `none`, `gaussian`, `median`. _Default_: `none`
- `--blur_amount`: Amount of blur to apply (use odd integers only). Use with `--blur_type`. _Default_: `1`
- `--max_size`: Maximum width or height of the output images. _Default_: `512`
- `--force_max`: forces the resize to the max size (by default `--max_size` only scales down)
- `--direction`: Paired Direction. For use with pix2pix process. _Options_: `AtoB`,`BtoA`. _Default_: `AtoB`
- `--mirror`: Adds mirror augmentation.
- `--rotate`: Adds 90 degree rotation augmentation.
- `--border_type`: Border style to use when using the `square` process type _Options_: `stretch`,`reflect`,`solid` (`solid` requires `--border-color`) _Default_: `stretch`
- `--border_color`: border color to use with the `solid` border type; use BGR values from 0 to 255 _Example_: `255,0,0` is blue
- `--height`: height of crop in pixels; use with `--process_type crop` or `--process_type resize` (when used with `resize` it will distort the aspect ratio)
- `--width`: width of crop in pixels; use with `--process_type crop` or `--process_type resize` (when used with `resize` it will distort the aspect ratio)
- `--shift_y`: y (Top to bottom) amount to shift in pixels; negative values will move it up, positive will move it down; use with `--process_type crop`
- `--shift_x`: x (Left to right) amount to shift in pixels; negative values will move it left, positive will move it right; use with `--process_type crop`
- `--file_extension`: file format to output _Options_: `jpg`,`png` _Default_: `png`

### dedupe.py

Remove duplicate images from your dataset

`python dedupe.py --input_folder /Users/khaledkaddal/Desktop/resense/Gearloose/DataSets/Sunsets/test --output_folder /Users/khaledkaddal/Desktop/resense/Gearloose/DataSets/Sunsets/2_output/test/ --relative`

- `--absolute`: Use absolute matching. _Default_
- `--avg_match`: average pixel difference between images (use with `--relative`) _Default_: `1.0`
- `--file_extension`: file format to output _Options_: `jpg`,`png` _Default_: `png`
- `--input_folder`: Directory path to the inputs folder. _Default_: `./input/`
- `--output_folder`: Directory path to the outputs folder. _Default_: `./output/`
- `--relative`: Use relative matching.
- `--verbose`: Print progress to console.

#### Basic usage (absolute)

`python dedupe.py --input_folder path/to/input/ --output_folder path/to/output/`

#### Basic usage (relative)

`python dedupe.py --input_folder path/to/input/ --output_folder path/to/output/ --relative`

### multicrop.py

This tool produces randomized multi-scale crops. A video tutorial is [here](https://youtu.be/0yj8B2x62EA)

- `--input_folder`: Directory path to the inputs folder. _Default_: `./input/`
- `--output_folder`: Directory path to the outputs folder. _Default_: `./output/`
- `--file_extension`: file format to output _Options_: `jpg`,`png` _Default_: `png`
- `--max_size`: Maximum width and height of the crop. _Default_: `None`
- `--min_size`: Minimum width and height of the crop. _Default_: `1024`
- `--resize`: size to resize crops to (if `None` it will default to `min_size`). _Default_: `None`
- `--no_resize`: If set the crops will not be resized. _Default_: `False`
- `--verbose`: Print progress to console.

### sort.py

- `--file_extension`: file format to output _Options_: `jpg`,`png` _Default_: `png`
- `--verbose`: Print progress to console.
- `--input_folder`: Directory path to the inputs folder. _Default_: `./input/`
- `--output_folder`: Directory path to the outputs folder. _Default_: `./output/`
- `--process_type`: Process to use. _Options_: `sort`,`exclude` _Default_: `exclude`
- `--max_size`: Maximum width or height of the output images. _Default_: `2048`
- `--min_size`: Minimum width or height of the output images. _Default_: `1024`
- `--min_ratio`: Ratio of image (height/width). _Default_: `1.0`
- `--exact`: Match to exact specs. Use `--min_size` for shorter dimension, `--max_size` for longer dimension

### interactive.py

[YouTube Demo](https://www.youtube.com/watch?v=tUzUJNrSAu8)

### rotate.py

### video-to-frames.py

- `-v`,`--video_path`: Path of the video file to be extracted.
- `-o`,`--output_folder`: Directory path to the outputs folder.
- `-f`,`--frames`: Numbers of frames to be skiped.

### coloring.py

```
python coloring.py
```
