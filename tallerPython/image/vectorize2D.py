#
# http://technicaldiscovery.blogspot.com.ar/2011/06/speeding-up-python-numpy-cython-and.html
#
import numpy 

a = numpy.asarray ([0.0 for i in range(100)]).reshape(10,10)

print(type(a))


dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy

def py_update(u):
    nx, ny = u.shape
    for i in numpy.arange(1,nx-1):
        for j in numpy.arange(1, ny-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))

def num_update(u):
    u[1:-1,1:-1] = ((u[2:,1:-1]+u[:-2,1:-1])*dy2 + 
        (u[1:-1,2:] + u[1:-1,:-2])*dx2) / (2*(dx2+dy2))


def calc(N, Niter=100, func=num_update, args=()):
    u = numpy.zeros([N, N])
    u[0] = 1
    for i in range(Niter):
        func(u,*args)
    return u


#print(calc(10, 10, func= num_update))
#print(calc(10, 10, func= py_update))


#u = numpy.zeros([10, 10])
#u[0] = 1

#a = numpy.zeros([10, 10])
a[0] = 1.0
u = a

print(type(u), u.shape)
for i in range(10):
    u[1:-1,1:-1] = ((u[2:,1:-1]+u[:-2,1:-1])*dy2 + 
        (u[1:-1,2:] + u[1:-1,:-2])*dx2) / (2*(dx2+dy2))


    #num_update(u)

print(u)    
