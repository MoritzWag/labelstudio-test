import os
import json
import pdb
import pandas as pd
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="store annotation results from respective user")
    parser.add_argument('--path', type=str, default=".",
                        help='path were user folders are stored')
    parser.add_argument('--user', type=str, default='moritz',
                        help='user for whom the results shall be retrieved')
    parser.add_argument('--project_name', type=str, default='ma',
                        help='the project name, each user can specify (should be identical in best case)')
    args = parser.parse_args()
    return args


def retrieve_annotations(args):
    """[summary]

    Args:
        path ([type]): [description]
    """
    path = args.path
    user = args.user
    project_name = args.project_name

    absolute_path = f"{path}/{user}/{project_name}/completions"

    df = pd.DataFrame(columns=['file', 'label'])

    for json_file in os.listdir(absolute_path):
        with open(f"{absolute_path}/{json_file}", "r") as read_file:
            data = json.load(read_file)
            choice = data['completions'][0]['result'][0]['value']['choices']
            instance = {'file': json_file, 'label': choice}
            df = df.append(instance, ignore_index=True)

    df.to_csv(f"./{user}_annotations.csv")


if __name__ == "__main__":
    args = parse_args()
    retrieve_annotations(args)
