# labelstudio-test
This is a small repository to preliminary play with the features of LabelStudio

## Installation

1. install all packages in `requirements.txt`

2. install labelstudio via `pip install label-studio`


## Setting up project
To set up a project, a variety of options are offered, whereby the method distinguishes between `single image annotation` and `multi image annotation` tasks.

### Single Image Annotation
1. define folder for user, e.g. `moritz`

2. setup a `config.xml` file which entails the label configuration, e.g. which labels to choose from.

3. Change in the users directory, e.g. `cd moritz`

3. Initialize the project with the following command:
`label-studio init <project_name> --input_path<where the image data is stored> --input-format image-dir --label-config ../config.xml --allow-serving-local-files`

4. Start labeling at local host:
`label-studio start <project_name>`

### Multi Image Annotation
To be discussed. To fully leverage their multi image classification scheme, I still have problems with specifying valid URLs for the images, which are required.
Therefore, I suggest a workaround by just merging the low- and high-energy images.
This can be done by running the following command in the terminal:
`python merge_images.py`

As we now have two images in one, we can simply proceed as in the 'Single Image Annotation' case. Whether this is a valid approach should be discussed.

## Start Annotation
For annotation just follow the instruction on the website. It is very intuitive.
Every step you process, is directly synchronized with your local folder.
All results can be found in the folder `completions`.



## Store Results
To store the results, run the following command from the parent directory:
`python store_results.py --path <default> --user <your username>`

Then, a csv file is stored with the username
