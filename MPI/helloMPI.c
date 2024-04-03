#include <mpi.h>                                        //line 1
#include <stdio.h>                                      //line 2

int main( int argc, char **argv ) {                     //line 3
    int rank, size;                                     //line 4
    MPI_Init( &argc, &argv );                           //line 5
    MPI_Comm_rank( MPI_COMM_WORLD, &rank );             //line 6
    MPI_Comm_size( MPI_COMM_WORLD, &size );             //line 7
    printf( "Hello from process %d/%d\n", rank, size ); //line 8
    MPI_Finalize( );                                    //line 9
    return 0;                                           //line 10
}
