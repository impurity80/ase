#!/bin/bash

#
#$ -q all.q
#$ -pe mpi_16 16
#$ -N vasp_oct_tet
#$ -o run.out
#$ -e run.err
#$ -V
#$ -cwd
#

time mpirun -np $NSLOTS vasp_std
