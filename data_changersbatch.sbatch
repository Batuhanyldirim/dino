#!/usr/bin/env bash
#SBATCH --mem 10GB
#SBATCH --gres gpu:3
#SBATCH --cpus-per-task 8
#SBATCH --constraint rivendell
#SBATCH --time 48:00:00
#SBATCH --mail-type FAIL
#SBATCH --mail-user batuhany@kth.se
#SBATCH --error /Midgard/home/%u/dino/logs/%J_slurm.err
#SBATCH --output /Midgard/home/%u/dino/logs/%J_slurm.out

echo "Starting job ${SLURM_JOB_ID} on ${SLURMD_NODENAME}"
nvidia-smi
. ~/miniconda3/etc/profile.d/conda.sh
pushd ~/dino
conda activate dino

python main_dino.py --data_path /local_storage/datasets/voc2012/changed_data \
    --output_dir /local_storage/users/batuhany/dino/checkpoints \
    --num_workers 4