from skimage import io, exposure
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = io.imread('colorful-2468874_640.jpg')

# Display the original image
plt.subplot(1, 3, 1)
plt.imshow(I)
plt.title('Original Image')

# Add salt and pepper noise
Isp = I + np.random.choice(
    [0, 1], size=I.shape, p=[0.97, 0.03])
plt.subplot(1, 3, 2)
plt.imshow(Isp)
plt.title('Image with Salt & Pepper Noise')

# Add Gaussian noise
Ig = I + np.random.normal(scale=0.02, size=I.shape)
plt.subplot(1, 3, 3)
plt.imshow(Ig)
plt.title('Image with Gaussian Noise')

plt.show()