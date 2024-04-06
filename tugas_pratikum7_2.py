import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import log10, sqrt


# citra = cv2.imread('Data/logo_polindra_noise.png', 0)
#Carilah terkait Mean Square Error (MSE) dan Peak Signal-to-Noise Ratio (PSNR) beserta implementasinya pada python
def PSNR(gambar_asli, gambar_asli2):
    mse = np.mean((gambar_asli - gambar_asli2) ** 2)
    if mse == 0:
        return 100
    pixel = 255.0
    psnr = 20 * log10(pixel / sqrt(mse))
    return psnr
#------------------------------------------------------------------------------------------------------------------
def main():
    gambar_asli = cv2.imread('Data/logo_polindra_asli.jpeg')
    gambar_noise = cv2.imread('Data/logo_polindra_noise.png')
    noise_remove = cv2.imread('Data/logo_polindra_noise.png')
    noise_remove = cv2.medianBlur(noise_remove, 7)
    gambar_asli = cv2.resize(gambar_asli, (312, 312))
    gambar_noise = cv2.resize(gambar_noise, (312, 312))
    noise_remove = cv2.resize(noise_remove, (312, 312))

    psnr_gambar_noise = PSNR(gambar_asli, gambar_noise)
    psnr_noise_remove = PSNR(gambar_noise, noise_remove)
    psnr_final = PSNR(gambar_asli, noise_remove)

    print(f"PSNR dan MSE antara gambar logo polindra_asli dan logo_polindra_noise: {psnr_gambar_noise:.2f}") #tambahkan :.2f jika nilai nya pengen lebih sederhana
    print(f"PSNR dan MSE antara gambar logo_polindra_noise dan hasil noise removal tugas 1: {psnr_noise_remove:.2f}")
    print(f"PSNR dan MSE antara gambar logo_polindra_asli dan hasil noise removal tugas 1: {psnr_final:.2f}")
    
    cv2.imshow('Gambar_Asli', gambar_asli)
    cv2.imshow('Gambar_Noise', gambar_noise)
    cv2.imshow('Gambar_noise_remove', noise_remove)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


if __name__ == "__main__":
    main()
