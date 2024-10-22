from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = 100
    comm.send(data, dest=1)
    print(f"Operation {rank} sent the message {data} and waited for the sending to complete")

elif rank == 1:
    data = comm.recv(source=0)
    print(f"Process {rank} received the message: {data}")
MPI.Finalize()