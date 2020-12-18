import os
import argparse
from shutil import copyfile


def walk_and_copy(src, dest):
    for root, dirs, files in os.walk(src):
        for file in files:
            if file == '.DS_Store':
                continue
            file_path = os.path.join(root, file)
            copyfile(file_path, os.path.join(dest, file))


def parse_args():
    parser = argparse.ArgumentParser(description='Merge all images into a single folder')
    parser.add_argument('sources', type=str, nargs='+', help='a list of directories that contains images')
    parser.add_argument('destination', type=str, help='directory that contains all images')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    srcs = args.sources
    dest = args.destination

    if dest not in os.listdir():
        os.mkdir(dest)
    for src in srcs:
        walk_and_copy(src, dest)
