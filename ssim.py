from skimage import io, img_as_float
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np

def calculate_image_distortion(image1, image2):
    # Read the images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    img2 = cv2.resize(img2, (0, 0), fx=0.25, fy=0.25)

    # Convert the images to floating-point format
    img1 = img_as_float(img1)
    img2 = img_as_float(img2)

    # Calculate SSIM between the two images
    ssim_value = ssim(img2, img1, channel_axis= 2)

    # Return the SSIM value as a measure of image distortion
    return ssim_value

def calculate_mse(image1, image2):
    # Calculate the mean square error between the two images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    img2 = cv2.resize(img2, (0, 0), fx=0.25, fy=0.25)

    mse = np.mean((img1 - img2) ** 2)
    return mse

def calculate_psnr(mse):
    # Calculate the peak signal-to-noise ratio between the two images
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))


if __name__ == '__main__':
    ssim = calculate_image_distortion('hasilKalib/DSC02052.JPG', 'uji/data_malaria/DSC02024.JPG')
    print("SSIM: ", ssim)

    MSE = calculate_mse('hasilKalib/DSC02052.JPG', 'uji/data_malaria/DSC02024.JPG')
    print("MSE: ", MSE)

    PSNR = calculate_psnr(MSE)
    print("PSNR: ", PSNR)
