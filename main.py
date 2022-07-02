
from PIL import Image                                                  # Necessary packages
import numpy as np
import matplotlib.pyplot as plt


img = np.array(Image.open(r'C:\Users\Ieva\NumPypicture\dog.jpg'))     # Opening image "dog.jpg"

print(type(img))                                                      # Checking images type
print(img.dtype)                                                      # Checking images dtype
print(img.shape)                                                      # Checking images shape

# plt.imshow(img) - for seeing original image
# plt.show()


a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13,\              # Dividing image to equal 20 horizontal parts
a14, a15, a16, a17, a18, a19, a20 = np.hsplit(img, 20)

plt.imshow(a1)                                                        # For seeing every image part that was cut
# plt.show()
plt.imshow(a2)
# plt.show()
plt.imshow(a3)
# plt.show()
plt.imshow(a4)
# plt.show()
plt.imshow(a5)
# plt.show()
plt.imshow(a6)
# plt.show()
plt.imshow(a7)
# plt.show()
plt.imshow(a8)
# plt.show()
plt.imshow(a9)
# plt.show()
plt.imshow(a10)
# plt.show()
plt.imshow(a11)
# plt.show()
plt.imshow(a12)
# plt.show()
plt.imshow(a13)
# plt.show()
plt.imshow(a14)
# plt.show()
plt.imshow(a15)
# plt.show()
plt.imshow(a16)
# plt.show()
plt.imshow(a17)
# plt.show()
plt.imshow(a18)
# plt.show()
plt.imshow(a19)
# plt.show()
plt.imshow(a20)
# plt.show()


c1 = np.concatenate((a1, a3, a5, a7, a9, a11, a13, a15, a17, a19,               # Joining separated image parts in
                     a2, a4, a6, a8, a10, a12, a14, a16, a18, a20), axis=1)     # different order and creating 2 images

print(type(c1))                                                                 # Checking images type
print(c1.dtype)                                                                 # Checking images dtype
print(c1.shape)                                                                 # Checking images shape


b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11,\                                  # Dividing image to equal 29
b12, b13, b14, b15, b16, b17, b18, b19, b20, b21,\                              # vertical parts
b22, b23, b24, b25, b26, b27, b28, b29 = np.split(c1, 29)

plt.imshow(b1)                                                                  # For seeing every image part
# plt.show()                                                                    # that was cut
plt.imshow(b2)
# plt.show()
plt.imshow(b3)
# plt.show()
plt.imshow(b4)
# plt.show()
plt.imshow(b5)
# plt.show()
plt.imshow(b6)
# plt.show()
plt.imshow(b7)
# plt.show()
plt.imshow(b8)
# plt.show()
plt.imshow(b9)
# plt.show()
plt.imshow(b10)
# plt.show()
plt.imshow(b11)
# plt.show()
plt.imshow(b12)
# plt.show()
plt.imshow(b13)
# plt.show()
plt.imshow(b14)
# plt.show()
plt.imshow(b15)
# plt.show()
plt.imshow(b16)
# plt.show()
plt.imshow(b17)
# plt.show()
plt.imshow(b18)
# plt.show()
plt.imshow(b19)
# plt.show()
plt.imshow(b20)
# plt.show()
plt.imshow(b21)
# plt.show()
plt.imshow(b22)
# plt.show()
plt.imshow(b23)
# plt.show()
plt.imshow(b24)
# plt.show()
plt.imshow(b25)
# plt.show()
plt.imshow(b26)
# plt.show()
plt.imshow(b27)
# plt.show()
plt.imshow(b28)
# plt.show()
plt.imshow(b29)
# plt.show()


c2 = np.concatenate((b1, b3, b5, b7, b9, b11, b13, b15, b17, b19, b21,          # Joining separated image parts in
                     b23, b25, b27, b29, b2, b4, b6, b8, b10, b12,              # different order and creating 4 images
                     b14, b16, b18, b20, b22, b24, b26, b28), axis=0)


pil_img = Image.fromarray(np.uint8(c2))                                         # Saving latest image
pil_img.save(r'C:\Users\Ieva\NumPypicture\dog1.jpg')                            # by the name "dog1.jpg"


img1 = np.array(Image.open(r'C:\Users\Ieva\NumPypicture\dog1.jpg'))             #  Open image "dog1.jpg"
# plt.imshow(img1)
# plt.show()                                                                    # For seeing image
# print(type(img1)) - Checking images type
# print(img1.dtype) - Checking images dtype
# print(img1.shape) - Checking images shape




d1,d2 = np.split(img1, 2)                                                      # Dividing image to equal vertical parts
# plt.imshow(d1) - For seeing both images
# plt.show()
# plt.imshow(d2)
# plt.show()


c3 = np.concatenate((d1,d2), axis = 1)                                         # Joining images for final image
plt.imshow(c3)
plt.show()                                                                     # For seeing both image
print(type(c3))                                                                # Checking images type
print(c3.dtype)                                                                # Checking images dtype
print(c3.shape)                                                                # Checking images shape

pil_img = Image.fromarray(np.uint8(c3))                                        # Saving final image
pil_img.save(r'C:\Users\Ieva\NumPypicture\dogFinal.jpg')                       # by the name "dogFinal.jpg"