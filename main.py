#Imports
from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image
import os


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments
        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    ds = Dataset(annotation_file, transforms) #Dataset object for performing the trasforms on the images
    dl = Download() #Download class object for dowloading and saving the images in the jsonl file

    #Print image names and their captions from annotation file using dataset object
    for i in range(ds.__len__()): #traversing the jsonl file
        obj = ds.__getann__(i) #extracting the dictionary from the list of disctionaries in the jsonl file
        print("Name: ", obj["file_name"]) #name of file
        print("Captions:") #printing the captions
        for caps in obj["captions"]:
            print(caps["caption"])

    #Download images to ./data/imgs/ folder using download object
    for i in range(ds.__len__()): 
        obj = ds.__getann__(i)
        dl("./data/imgs/" + obj["file_name"], obj["url"]) #downloading and saving the images

    #Transform the required image (roll number mod 10) and save it seperately
    try:
        os.makedirs(f'{outputs}', exist_ok = True)
    except Exception:
        pass
    im = Image.open("./data/imgs/9.jpg")
    image_list = ds.__transformitem__(im)
    for i in range(len(image_list)):
        image_list[i].save(f"{outputs}/{i + 1}.jpg")

    #Get the predictions from the captioner for the above saved transformed image
    model = ImageCaptioningModel() #model object or the ImageCaptioningModel class
    for i, img in enumerate(image_list): #traversing the list of transformed images in ls
        print(f"\nGenerated captions for the Image {i+1} : ") #printing the generated captions using model
        print(model(f"Output/{i+1}.jpg", 3))

def main():
    captioner = ImageCaptioningModel()
    #performing the required 7 trnasforms(1st one being the original image)
    #height of image = 428 so rescale parameter for 2x = 428*2 = 856(int passed)
    #width of image = 639 so rescale parameter for 0.5x = 639/2,428/2 = 319,214 (tuple passed)
    experiment('./data/annotations.jsonl', captioner, [RotateImage(0), FlipImage("horizontal"), BlurImage(1), RescaleImage(856), RescaleImage((319, 214)), RotateImage(-90), RotateImage(45)], './Output')  # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
