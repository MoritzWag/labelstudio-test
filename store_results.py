import os
import json
import pdb
import pandas as pd
import argparse
import copy


def parse_args():
    parser = argparse.ArgumentParser(description="store annotation results from respective user")
    parser.add_argument('--path', type=str, default=".",
                        help='path were user folders are stored')
    parser.add_argument('--users', nargs='+', default=['moritz'],
                        help='user for whom the results shall be retrieved')
    parser.add_argument('--project_name', type=str, default='annotation',
                        help='the project name, each user can specify (should be identical in best case)')
    args = parser.parse_args()
    return args


def retrieve_annotations(args):
    """[summary]

    Args:
        path ([type]): [description]
    """
    path = args.path
    users = args.users
    project_name = args.project_name


    column_names = copy.deepcopy(args.users)
    column_names.append('file')
    column_names.append('consensus')
    #df_all = pd.DataFrame(columns=column_names)
    df_all = pd.DataFrame(columns=['file'])
    count = 0
    for user in users:
        df = pd.DataFrame(columns=['file', 'user'])
        absolute_path = f"{path}/{user}/{project_name}/completions"
        for json_file in os.listdir(absolute_path):
            with open(f"{absolute_path}/{json_file}", "r") as read_file:
                data = json.load(read_file)
                choice = data['completions'][0]['result'][0]['value']['choices']
                instance = {'file': json_file, f"{user}": choice}
                df = df.append(instance, ignore_index=True)
        df.to_csv(f"./{user}_annotations.csv")
        if count == 0:
            df_all[user] = df[user]
            df_all['file'] = df['file']
        else:
            df_all = pd.merge(df_all, df, how='outer', on='file', left_index=True, right_index=True)


        count += 1
    df_all = df_all.dropna(axis=1, how='all')
    df_all['consensus'] = df_all.apply(lambda row: row.moritz == row.jann == row.steffen, axis=1)
    df_all.to_csv("annotations.csv")


if __name__ == "__main__":
    args = parse_args()
    retrieve_annotations(args)
