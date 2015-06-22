import numpy
from scipy import misc
from scipy import ndimage
from PIL import Image
import matplotlib.pyplot as plt

def linear_equation(x0, y0, x1, y1):
    deltaX = x1 - x0
    deltaY = y1 - y0
    a = deltaY / deltaX
    b = y1 - a * x1
    return (a, b)

def linear_piece(v):
    (a1,b1) = (linear_equation(0, 0, 30, 20))
    (a2, b2) = (linear_equation(30, 20, 150, 120))
    (a3, b3) = (linear_equation(150, 120, 255, 255))

    if v <= 150:
        if v <= 30:
            v = a1 * v + b1 
        else:
            v = a2 * v + b2
    else:
        # v > 150
        v = a3 * v + b3
        pass
    if v < 0:
        v = 0
    if v > 255:
        v = 255
    return v

vlinear_piece = numpy.vectorize(linear_piece)

# Lectura de la imagen
im = Image.open("dna.jpeg")

# Conversión a array numpy
pix = numpy.array(im)

# Lectura de las propiedades de pix
print("formato NUMPY ", pix.shape, pix.dtype, pix.max(), pix.min(), pix.mean())

th =  1.0 * pix.mean()
mx = pix.max()

(a, b) = linear_equation(0, th, mx, 255)
print ("a b ", a, b)

pix[pix <  th] = 0
pix = a * pix  + b
pix[pix < 0] = 0

print("formato recortado ", pix.shape, pix.dtype, pix.max(), pix.min(), pix.mean())

pix  = vlinear_piece(pix)

deriv = ndimage.gaussian_filter(pix, 3, order = 2)
print("deriv: ", deriv.min(), deriv.max())
g = pix - deriv 
print("g: ", g.min(), g.max())
k = 0.3
enhan = pix + k * g 
print(enhan.min(), enhan.max())


im_p = numpy.uint8(enhan)
im_png = Image.fromarray(im_p)
misc.imsave('gaussian_filter.png', im_png)
