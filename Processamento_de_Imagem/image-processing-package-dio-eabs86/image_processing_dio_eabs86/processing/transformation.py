from skimage.transform import resize



# a ideia desta função é somente utilizá-la quando tiver imagens muito grandes e você quiser diminuí-las.

def resize_image(image, proportion):
    assert 0<= proportion <=1, "Specify a valid proportion between 0 and 1"
    height = round(image.shape[0]*proportion)
    width = round(image.shape[1]*proportion)
    image_resized = resize(image, (height,width),anti_aliasing=True)
    
    return image_resized