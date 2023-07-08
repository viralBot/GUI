#Imports
import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        with jsonlines.open(annotation_file, 'r') as jsonl_f:
            self.lst = [im for im in jsonl_f]
        self._transforms = transforms
     

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.lst)


    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        return self.lst[idx]
        

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        lst = [] #list for storing all the transformed images
        for transform in self._transforms:
            im = transform(path)
            lst.append(im)
        return lst #list returned
