
import argparse
import os
import numpy as np
import pdb
import matplotlib.pyplot as plt
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description="get example data")
    parser.add_argument('--path', type=str, default='./data/example_arrays_labelling_tool')
    parser.add_argument('--storage_path', type=str, default='./data')
    args = parser.parse_args()
    return args


def get_data(args):

    count = 0
    for array in os.listdir(args.path):
        img = np.load(f"{args.path}/{array}")

        # process low energy
        img_le = img[0, :, :]
        img_low = Image.fromarray(img_le)
        plt.imsave(f"{args.storage_path}/low-energy/{array[:-4]}.png", img_low, cmap='gray')

        # process high energy
        img_high = img[1, :, :]
        img_high = Image.fromarray(img_high)
        plt.imsave(f"{args.storage_path}/high-energy/{array[:-4]}.png", img_high, cmap='gray')

        img_low = Image.open(f"{args.storage_path}/low-energy/{array[:-4]}.png")
        img_high = Image.open(f"{args.storage_path}/high-energy/{array[:-4]}.png")

        images = [img_low, img_high]

        widhts, heights = zip(*(i.size for i in images))
        total_width = sum(widhts)
        max_height = max(heights)

        combined_image = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for im in images:
            combined_image.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        combined_image.save(f'{args.storage_path}/combined/combined_{count}.jpg')

        count += 1


if __name__ == "__main__":
    args = parse_args()
    get_data(args=args)
