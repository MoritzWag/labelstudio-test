import os
import json
import pdb
import pandas as pd
import argparse
from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(description="create relevant json files from images")
    parser.add_argument('--path', type=str, default="./data",
                        help='path were user folders are stored')
    args = parser.parse_args()
    return args


def merge_images(args):
    """[summary]

    Args:
        args ([type]): [description]
    """
    path = args.path
    absolute_path = os.path.abspath(path)

    path_low_energy = f"{absolute_path}/low-energy/"
    path_high_energy = f"{absolute_path}/high-energy/"

    count = 0

    for img1, img2 in zip(os.listdir(path_low_energy),
                          os.listdir(path_high_energy)):
        img_low = Image.open(f"{path_low_energy}{img1}")
        img_high = Image.open(f"{path_high_energy}{img2}")

        images = [img_low, img_high]

        widhts, heights = zip(*(i.size for i in images))
        total_width = sum(widhts)
        max_height = max(heights)

        combined_image = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for im in images:
            combined_image.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        combined_image.save(f'{absolute_path}/combined/combined_{count}.jpg')

        count += 1


if __name__ == "__main__":
    args = parse_args()
    merge_images(args)
