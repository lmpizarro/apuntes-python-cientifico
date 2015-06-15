import numpy
import sys
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
N=1000000
mu = [1,10,100,50, 2,20,200,30]
sigma = [2,3,4,5, 6,7,8,9]
n = [N, N, N, N, N, N, N, N]

def func (a, b, c):
    v = numpy.asarray([numpy.random.normal(a,b) for i in range(c)])
    w = 1.0 / v
    return w.mean()

#initializing variables. mpi4py requires that we pass numpy objects.
integral = numpy.zeros(1)
recv_buffer = numpy.zeros(1)

local_mu = mu[rank]
local_sigma = sigma[rank]
local_n = n[rank]

integral[0] = func (local_mu, local_sigma, local_n)

print ("Resultado del nodo %d para %d puntos,  inverse mean %f" % (rank, n[rank], integral[0]))

# communication
# root node receives results from all processes and sums them
if rank == 0:
        total = integral[0]
        for i in range(1, size):
                comm.Recv(recv_buffer, ANY_SOURCE)
                total += recv_buffer[0]
else:
        # all other process send their result
        comm.Send(integral)

# root process prints results
if comm.rank == 0:
        print "Total ", total
