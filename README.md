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
`label-studio start <project_name>

### Multi Image Annotation 


## Start Annotation 



## Store Results
