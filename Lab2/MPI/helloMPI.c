// #include <mpi.h>                                        //line 1
// #include <stdio.h>                                      //line 2

// int main(int argc, char* argv[]) {
//   int rank, size; 

//   MPI_Init(&argc, &argv); // Initialize MPI environment 
//   MPI_Comm_rank(MPI_COMM_WORLD, &rank); // Get process rank
//   MPI_Comm_size(MPI_COMM_WORLD, &size); // Get total processes 

//   printf("Hello World from process %d of %d\n", rank, size);  

//   MPI_Finalize(); // Finalize MPI environment 
//   return 0;
// }

/*
  "Hello World" MPI Test Program
*/
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <mpi.h>

int main(int argc, char **argv){
    char buf[256];
    int my_rank, num_procs;

    /* Initialize the infrastructure necessary for communication */
    MPI_Init(&argc, &argv);

    /* Identify this process */
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

    /* Find out how many total processes are active */
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    /* Until this point, all programs have been doing exactly the same.
       Here, we check the rank to distinguish the roles of the programs */
    if (my_rank == 0) {
        int other_rank;
        printf("We have %i processes.\n", num_procs);

        /* Send messages to all other processes */
        for (other_rank = 1; other_rank < num_procs; other_rank++)
        {
            sprintf(buf, "Hello %i!", other_rank);
            MPI_Send(buf, 256, MPI_CHAR, other_rank,
                     0, MPI_COMM_WORLD);
        }

        /* Receive messages from all other processes */
        for (other_rank = 1; other_rank < num_procs; other_rank++)
        {
            MPI_Recv(buf, 256, MPI_CHAR, other_rank,
                     0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("%s\n", buf);
        }

    } else {

        /* Receive message from process #0 */
        MPI_Recv(buf, 256, MPI_CHAR, 0,
                 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        assert(memcmp(buf, "Hello ", 6) == 0);

        /* Send message to process #0 */
        sprintf(buf, "Process %i reporting for duty.", my_rank);
        MPI_Send(buf, 256, MPI_CHAR, 0,
                 0, MPI_COMM_WORLD);

    }

    /* Tear down the communication infrastructure */
    MPI_Finalize();
    return 0;
}