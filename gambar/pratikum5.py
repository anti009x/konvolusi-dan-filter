import cv2
import matplotlib.pyplot as plt
import numpy as np

inp = cv2.imread('pemandangan.jpg')
cv2.imshow('pemandangan',inp)
plt.imshow(inp)
plt.title("Gambar Ori RGB")
plt.show()

inpRGB = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)
inpRGB = cv2.imread('pemandangan.jpg')
cv2.imshow('pemandangan',inpRGB)
plt.imshow(inpRGB)
plt.title("Gambar Ori RGB")
plt.show()
tombol = cv2.waitKey(0)
if tombol == 27:
    cv2.destroyAllWindows()

