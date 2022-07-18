from ast import arg
import os
import json
import sys
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Transforms labeller JSON data into JSON data structure suitable for classifier')
parser.add_argument('--json_path', metavar='json_path', type=str, help='The path to the directory containing the JSONs')
parser.add_argument('--jpg_path', metavar='jpg_path', type=str, help='The path to the directory containing the JPG images.')

args = parser.parse_args()

path_to_json = args.json_path
path_to_jpg = args.jpg_path

if not os.path.isdir(path_to_json):
    print("This path doesn't exist, mate.")
    sys.exit()

# appends onto array all the json in the specified directory path (i.e. ends with .json)
json_files = [img_json for img_json in os.listdir(path_to_json) if img_json.endswith('.json')]
jpg_files = [img_jpg for img_jpg in os.listdir(path_to_jpg) if img_jpg.endswith('.jpg')]

# NOTE TO US - remember to add that extra forward slash to the path argument since it's going to just straight up concatenate
# below includes a whole lot of hacky stuff, and is truly "works on my computer" type of technology. will work on that later

label_dict = {}

label_to_directory = {
    'p_stop': './pedestrian_stop/',
    'p_walk': './pedestrian_walking/',
    'stop_sign': './stop_sign/',
    'face': './test_folder/'
}

for file in json_files:
    file_name = path_to_json + file
    jpg_name = file.replace('.json','') + '.jpg'

    f = open(file_name)

    data = json.load(f)

    label = data['shapes'][0]['label']
    points = data['shapes'][0]['points']
    left = points[0][0]
    top = points[0][1]
    right = points[1][0]
    bottom = points[1][1]

    if label in label_dict:
        label_dict[label] += 1
    else:
        label_dict[label] = 1

    if jpg_name in jpg_files:
        true_jpg_path = path_to_jpg + jpg_name
        img = Image.open(true_jpg_path)
        cropped_img = img.crop((left,top,right,bottom))
        if label in label_to_directory:
            save_directory = label_to_directory[label]
        else: 
            print('Improper label. Ooops!')
            sys.exit()
        cropped_img.save(save_directory + file.replace('.json','')+'_'+label+'_'+str(label_dict[label])+'.jpg')
        
print('Successful cropping.')
    