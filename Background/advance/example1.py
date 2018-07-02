from mpi4py import MPI

comm=MPI.COMM_WORLD

rank = comm.rank

if rank==0:
    data= (rank+1)*5
    comm.send(data,dest=1)
if rank==1:
    data=comm.recv(source=0)
    print (data)

#mpirun -n 2 ~/anaconda3/bin/python example1.py

