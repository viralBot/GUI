#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self._output_size = output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if(type(self._output_size) == tuple): #if output size is of type tuple
            w,h = self._output_size
            return image.resize((int(w),int(h))) #output matched to output size(h and w typecasted to int to keep argument type consistent in resize function)
        else:#if output size is an int
            w,h = image.size
            if w>=h:#case when h is smaller
                a_rat= w/h
                h = int(self._output_size)#h matched to output size
                w = int(a_rat * h)#w value changed as per the aspect ratio to keep aspect ratio same
            else:#case when w is smaller(vice versa of above case)
                a_rat= h/w
                w = int(self._output_size)
                h = int(a_rat * w)
            return image.resize((w,h))
            