import os
import json
import pdb
import pandas as pd
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="create relevant json files from images")
    parser.add_argument('--path', type=str, default="./data",
                        help='path were user folders are stored')
    parser.add_argument('--multi', type=bool, default=True,
                        help='user for whom the results shall be retrieved')
    args = parser.parse_args()
    return args


def assign_img_to_json(args):
    """[summary]

    Args:
        path ([type]): [description]
    """
    path = args.path
    multi = args.multi
    absolute_path = os.path.abspath(path)
    #absolute_path = path
    #absolute_path1 = absolute_path[1:]
    if multi:
        path_low_energy = f"{absolute_path}/low-energy/"
        path_high_energy = f"{absolute_path}/high-energy/"

        count = 0

        for img1, img2 in zip(os.listdir(path_low_energy),
                              os.listdir(path_high_energy)):

            # create dictionary with the right keys
            # dictionary = {'image1': f"http://0.0.0.0:8080/data/filename?d={path_low_energy}{img1}",
            #               'image2': f"http://0.0.0.0:8080/data/filename?d={path_high_energy}{img2}"}

            # dictionary = {'image1': f"http://0.0.0.0:8080{path_low_energy}{img1}",
            #               'image2': f"http://0.0.0.0:8080{path_high_energy}{img2}"}
            dictionary = {'image1': f"file://{path_low_energy}{img1}",
                          'image2': f"file://{path_high_energy}{img2}"}
            # dictionary = {'image1': f"{path_low_energy}{img1}",
            #               'image2': f"{path_high_energy}{img2}"}

            # save as unique json file
            with open(f"{absolute_path}/json_files/json{count}.json", "w") as json_file:
                json.dump(dictionary, json_file)

            count += 1

    else:
        path_all = f"{absolute_path}/data2/"
        count = 0
        for img, in zip(os.listdir(path_all)):
            dictionary = {'image': f"file://{path_all}{img}"}

            with open(f"{absolute_path}/json_files/json{count}.json", "w") as json_file:
                json.dump(dictionary, json_file)

            count += 1


if __name__ == "__main__":
    args = parse_args()
    assign_img_to_json(args)



# path = './data'

# assign_img_to_json(path=path, multi=False)
