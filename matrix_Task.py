from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 4

if rank == 0:
    A = np.random.randint(1, 10, (N, N), dtype=np.int64)  
    B = np.random.randint(1, 10, (N, N), dtype=np.int64)  
else:
    A = None
    B = np.empty((N, N), dtype=np.int64) 


local_A = np.empty((N // size, N), dtype=np.int64)

comm.Scatter(A, local_A, root=0)

comm.Bcast(B, root=0)

local_C = np.dot(local_A, B)

C = None
if rank == 0:
    C = np.empty((N, N), dtype=np.int64)

comm.Gather(local_C, C, root=0)

if rank == 0:
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix C (Result of A * B):")
    print(C)

# Finalize MPI
MPI.Finalize()
