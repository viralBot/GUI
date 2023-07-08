#Imports
from PIL import Image
from random import randrange

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self._shape = shape
        self._crop_type = crop_type
        

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        width, height = image.size
        if self._crop_type == 'random': #for random crop
            #left + cropped width + right = width of image, hence range of left is from 0 to width of image - cropped width (when right is 0)
            #similarly for top
            left = randrange(0, width - self._shape[0])
            top = randrange(0, height - self._shape[1])
        else:#for center crop
            #using symmetery and math, left and top expressions are:-
            left = (width - self._shape[0]) / 2
            top = (height - self._shape[1]) / 2
        right = left + self._shape[0]
        bottom = top + self._shape[1]
        im = image.crop((left, top, right, bottom))
        return im


 