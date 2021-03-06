__author__ = 'azrael'

import theano
import theano.tensor as T
import numpy as np
# Preproccessing the data script

def load_dataset(path):
    """
    Loads the dataset as a string file given the path of dataset.
    :param path: Path of the dataset.
    :return: String format of dataset
    """
    f = open(path, mode='r')
    x = f.read()
    return x

def remove_letters(dataset):
    """
    Remove some specific letters from the dataset.
    :param dataset: Input string file dataset
    :return: Dataset(string file) with removed values
    """
    remove_these_items = ['\xa4', '\xa9', '\xaa', '\xbb', '\xbf', '\xc3', '\xef']
    for item in remove_these_items:
        dataset = dataset.replace(item, '')
    dataset=dataset.replace('\xa0', ' ')
    return dataset

def one_hot_vec(data):
    """
    Creates a one hot vector representation of the letters
    :param data: Input string file dataset.
    :return: Dictionary of 1 hot input vectors of letters.
    """
    dict_letters = {}
    letters = set(list(data))
    idx = 0
    for letter in letters:
        temp = np.zeros(len(letters))
        temp[idx] = 1
        idx += 1
        dict_letters[letter] = temp
    return dict_letters



