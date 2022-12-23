from skimage.io import imread, imsave

def read_image(patch, is_gray=False):
    image = imread(path, as_gray= is_gray)
    return image

def save_image(image, path):
    imsave(path, image)
    