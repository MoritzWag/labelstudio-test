import os
import json
import pdb


def assign_img_to_json(path):
    """[summary]

    Args:
        path ([type]): [description]
    """
    absolute_path = os.path.abspath(path)
    #absolute_path = path
    #absolute_path1 = absolute_path[1:]
    path_low_energy = f"{absolute_path}/low-energy/"
    path_high_energy = f"{absolute_path}/high-energy/"

    count = 0
    for img1, img2 in zip(os.listdir(path_low_energy),
                          os.listdir(path_high_energy)):

        # create dictionary with the right keys
        # dictionary = {'image1': f"http://0.0.0.0:8080/data/filename?d={path_low_energy}{img1}",
        #               'image2': f"http://0.0.0.0:8080/data/filename?d={path_high_energy}{img2}"}

        dictionary = {'image1': f"http://0.0.0.0:8080{path_low_energy}{img1}",
                      'image2': f"http://0.0.0.0:8080{path_high_energy}{img2}"}
        # dictionary = {'image1': f"file///{path_low_energy}{img1}",
        #               'image2': f"file///{path_high_energy}{img2}"}
        # dictionary = {'image1': f"{path_low_energy}{img1}",
        #               'image2': f"{path_high_energy}{img2}"}

        # save as unique json file
        with open(f"{absolute_path}/json_files/json{count}.json", "w") as json_file:
            json.dump(dictionary, json_file)

        count += 1

# def assign_img_to_json_alternative(path):
#     """[summary]

#     Args:
#         path ([type]): [description]
#     """

#     absolute_path = os.path.abspath(path)





path = './data'

assign_img_to_json(path=path)
