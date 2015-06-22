#
# scipy: scipy.ndimage submodule dedicated to image processing
#
from scipy import ndimage
#
# Writing an array to a file
#
from scipy import misc
lena = misc.lena()
misc.imsave('lena.png', lena) # uses the Image module (PIL)

print ("información estadística media %f min %f max %f "% (lena.mean(), lena.min(), lena.max()) )


import matplotlib.pyplot as plt
plt.imshow(lena)
plt.gray()
plt.show()

blurred_lena = ndimage.gaussian_filter(lena, sigma=3)
plt.imshow(blurred_lena)
plt.gray()
plt.show()

very_blurred = ndimage.gaussian_filter(lena, sigma=5)
plt.imshow(very_blurred)
plt.gray()
plt.show()

print("local mean")
local_mean = ndimage.uniform_filter(lena, size=11)
plt.imshow(local_mean)
plt.gray()
plt.show()

#Increase contrast by setting min and max values:
plt.imshow(lena, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.gray()
plt.show()

# Draw Contour
plt.contour(lena, [60, 211])
plt.imshow(lena)
plt.gray()
plt.show()

# For fine inspection of intensity variations, use interpolation='nearest'
plt.imshow(lena[200:220, 200:220], cmap=plt.cm.gray)
plt.gray()
plt.show()

plt.imshow(lena[200:220, 200:220], cmap=plt.cm.gray, interpolation='nearest')
plt.gray()
plt.show()


#
# Creating a numpy array from an image file:
#
print( type(lena), lena.shape, lena.dtype)
print(type(type(lena)), type(lena.shape))

#
#
#
import numpy
for i in range(10):
    im = numpy.random.random_integers(0, 255, 10000).reshape((100, 100))
    misc.imsave('random_%02d.png' % i, im)


from glob import glob

filelist = glob('random*.png')
filelist.sort()

print(filelist)

