#! /bin/bash 




# source activate v_3
WORKDIR=/home/murota/Research/DimerMaster/sh
cd $WORKDIR





q=(0.9 0.8 1.0)
h=(1)
upperlim_h=${#h[@]}
upperlim_q=${#q[@]}


for ((j=0; j<=upperlim_q-1; j++)); do
    for ((i=0; i<=upperlim_h-1; i++)); do
        sbatch --job-name=d_h${h[$i]}_q${q[$j]} --output=logfile/dynamics/h${h[$i]}_q${q[$j]}.log main_dynamics.sh ${h[$i]} ${q[$j]}
    done
done