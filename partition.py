"""
partition dataset into training and testing
"""
import os


def data_partition(data_dir, percentage=0.15):
    """
    This function is going to create a testing directory that has the same structure as data_dir, next to data_dir
    :param data_dir: data location
    :param percentage: percentage of data to be testing set
    """
    file_name_levels = os.path.split(data_dir)
    TESTING_DIR = os.path.join(''.join(file_name_levels[:len(file_name_levels) - 1]), 'testing')
    label_dirs = os.listdir(data_dir)
    os.mkdir(TESTING_DIR)
    for label_dir in label_dirs:
        train_label_dir = os.path.join(data_dir, label_dir)
        if not os.path.isdir(train_label_dir):
            continue
        test_label_dir = os.path.join(TESTING_DIR, label_dir)
        os.mkdir(test_label_dir)
        samples = os.listdir(train_label_dir)
        n = len(samples)
        n_test = int(n * percentage)
        for sample in samples[:n_test]:
            os.rename(os.path.join(train_label_dir, sample), os.path.join(test_label_dir, sample))
