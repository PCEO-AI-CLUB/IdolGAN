import os
import cv2
from tqdm import tqdm
import random
import numpy as np


def gaussian_noisy(row, col, ch, sigma, image):
    gauss = np.random.normal(0, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy


def degrad_img(degrad_image):
    sigma = (random.random() * (6 - 1.5)) + 1.5  # min 1.5 1.5 0 100    max  6 4 10 60
    r = (random.random() * (4 - 1.5)) + 1.5
    delta = (random.random() * (10 - 0)) + 0
    q = int((random.random() * (100 - 60)) + 60)  # JPEG compression
    image = cv2.GaussianBlur(degrad_image, (0, 0), sigma)  # Gaussian blur

    new_size = int(512 / r)
    image = cv2.resize(image, (new_size, new_size), interpolation=cv2.INTER_LINEAR)  # image downsample
    image = gaussian_noisy(new_size, new_size, 3, delta, image)  # gaussian noise

    path_jpeg_downsample = ''  # you must fill in the path for the temp images. It is useless when the task is done.
    cv2.imwrite(path_jpeg_downsample, image, [int(cv2.IMWRITE_JPEG_QUALITY), q])  # png to jpeg
    image = cv2.imread(path_jpeg_downsample)
    image = cv2.resize(image, dsize=(512, 512), interpolation=cv2.INTER_LINEAR)
    return image


def degrad_img_list(path, img_list_path, output_path='degrad_image'):
    """
    Randomly degrade image for testing.

    :param path: path to the folder to save the degraded images
    :param img_list_path: list of paths to the images
    :param output_path: name of the folder to save the degraded images
    """
    if not os.path.exists(path + '/' + output_path):
        os.mkdir(path + '/' + output_path)

    for i, image_path in enumerate(tqdm(img_list_path)):
        image = cv2.imread(image_path)
        image = degrad_img(image)
        if image is not None:
            cv2.imwrite(path + '/' + output_path + '/' + str(image_path.split('\\')[-1].split('.')[0]) + '.jpg', image,
                        [int(cv2.IMWRITE_JPEG_QUALITY), 100])
