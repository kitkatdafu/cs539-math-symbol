import csv
import json
import argparse
import numpy as np
import os

def main():
    # create a parser for command line arguments
    parser = argparse.ArgumentParser(description='Convert COCO-json annotation format into GTDB-csv annotation format')
    parser.add_argument('json', type=str, help='COCO-json file')
    parser.add_argument('csv', type=str, help='GTDB-csv file, if the file does not exist, the program is going to create it')
    args = parser.parse_args()

    json_file = args.json # json file
    csv_file = args.csv # csv file

    file_suffix = csv_file.split('.')[0]

    with open(file_suffix + '_pdf', 'w') as f:
        f.write(file_suffix)

    with open(file_suffix, 'w') as anno_file:
        with open(csv_file, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            with open(json_file) as json_file: # open the json file
                json_load = json.load(json_file)
                annotations = json_load['annotations'] # extract annotations from json file
                image_id_map = {image_info['id']:int(image_info['file_name'].split('.')[0]) - 1 for image_info in json_load['images']}
                for annotation in annotations:
                    image_id = annotation['image_id'] # image_id
                    bbox = annotation['bbox'] # bbox
                    x_1 = bbox[0]
                    y_1 = bbox[1]
                    width = bbox[2]
                    height = bbox[3]
                    x_2 = x_1 + width
                    y_2 = y_1 + height
                    anno_file.write('all-images/' + str(image_id_map[image_id] + 1) + '\n')
                    csv_writer.writerow([image_id_map[image_id], x_1, y_1, x_2, y_2])


if __name__ == '__main__':
    main()
