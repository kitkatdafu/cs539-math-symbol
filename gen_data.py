import argparse
import os
import numpy as np
import shutil


def arg_parser():
    parser = argparse.ArgumentParser(description='Generate training/validation list')
    parser.add_argument('dataset', type=str, help='dataset name')
    parser.add_argument('--percentage', type=float, help='percentage to be training images', default='0.85')
    return parser.parse_args()

def main():
    args = arg_parser()
    image_dir_name = 'coarse_data'

    dataset = args.dataset
    train_percentage = args.percentage

    num_imgs = 0
    for root, dirs, files in os.walk(os.path.join(dataset, 'images', image_dir_name)):
        for name in files:
            if name != '.DS_Store':
                num_imgs += 1

    indices = np.random.RandomState(seed=42).permutation(num_imgs) + 1

    # create training_data and validation_data file
    with open(os.path.join(dataset, 'training_data'), 'w') as f:
        for i in range(0, int(train_percentage * num_imgs)):
            f.write(image_dir_name + '/' + str(indices[i]) + '\n')

    with open(os.path.join(dataset, 'validation_data'), 'w') as f:
        for i in range(int(train_percentage * num_imgs), num_imgs):
            f.write(image_dir_name + '/' + str(indices[i]) + '\n')

if __name__ == '__main__':
    main()
