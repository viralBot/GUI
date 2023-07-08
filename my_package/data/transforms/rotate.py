#Imports
from PIL import Image

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        self._degree = degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        img = sample.rotate(self._degree, Image.NEAREST, expand=1)
        return img
