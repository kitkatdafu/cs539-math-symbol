"""
partition dataset into training and testing
"""
import os
import random
import shutil


def slim(data_dir, percentage=0.10):
    label_dirs = os.listdir(data_dir)
    min_n = 100000000
    for label_dir in label_dirs:
        train_label_dir = os.path.join(data_dir, label_dir)
        if not os.path.isdir(train_label_dir):
            continue
        samples = os.listdir(train_label_dir)
        if len(samples) < min_n:
            min_n = len(samples)

    file_name_levels = os.path.split(data_dir)
    slim_testing_dir = os.path.join(''.join(file_name_levels[:len(file_name_levels) - 1]), 'slim_testing')
    slim_training_dir = os.path.join(''.join(file_name_levels[:len(file_name_levels) - 1]), 'slim_training')
    os.mkdir(slim_testing_dir)
    os.mkdir(slim_training_dir)
    for label_dir in label_dirs:
        train_label_dir = os.path.join(data_dir, label_dir)
        if not os.path.isdir(train_label_dir):
            continue

        slim_test_label_dir = os.path.join(slim_testing_dir, label_dir)
        os.mkdir(slim_test_label_dir)
        slim_training_label_dir = os.path.join(slim_training_dir, label_dir)
        os.mkdir(slim_training_label_dir)

        samples = os.listdir(train_label_dir)
        n_test = int(min_n * percentage)

        idx = random.sample(range(len(samples)), min_n)
        for i in range(len(samples)):
            if i in idx[:n_test]:
                shutil.copyfile(os.path.join(train_label_dir, samples[i]), os.path.join(slim_test_label_dir,
                                                                                        samples[i]))
            if i in idx[n_test:]:
                shutil.copyfile(os.path.join(train_label_dir, samples[i]), os.path.join(slim_training_label_dir,
                                                                                        samples[i]))


def data_partition(data_dir, percentage=0.1):
    """
    This function is going to create a testing directory that has the same structure as data_dir, next to data_dir
    :param data_dir: data location
    :param percentage: percentage of data to be testing set
    """
    file_name_levels = os.path.split(data_dir)
    testing_dir = os.path.join(''.join(file_name_levels[:len(file_name_levels) - 1]), 'testing')
    label_dirs = os.listdir(data_dir)
    os.mkdir(testing_dir)
    for label_dir in label_dirs:
        train_label_dir = os.path.join(data_dir, label_dir)
        if not os.path.isdir(train_label_dir):
            continue
        test_label_dir = os.path.join(testing_dir, label_dir)
        os.mkdir(test_label_dir)
        samples = os.listdir(train_label_dir)
        n = len(samples)
        n_test = int(n * percentage)
        for sample in samples[:n_test]:
            os.rename(os.path.join(train_label_dir, sample), os.path.join(test_label_dir, sample))
