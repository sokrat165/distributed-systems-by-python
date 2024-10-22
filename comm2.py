from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

tag = 123  

if rank == 0:
    data = "Hello from Rank 0"  
    request = comm.isend(data, dest=1, tag=tag)  
    print("Process 0 started sending without waiting")
    print("Process 0 is doing other tasks during the send")
    request.wait()  
    print("Process 0 finished sending")

elif rank == 1:
    request = comm.irecv(source=0, tag=tag)  
    print("Process 1 started receiving without waiting")
    time.sleep(2)  
    print("Process 1 is doing other tasks during the receive")
    data = request.wait()  
    print(f"Process 1 received: {data}")
MPI.Finalize()
