#!/usr/bin/env bash
#SBATCH --mem 10GB
#SBATCH --gres gpu:0
#SBATCH --cpus-per-task 8
#SBATCH --constraint shelob
#SBATCH --time 1:00:00
#SBATCH --mail-type FAIL
#SBATCH --mail-user batuhany@kth.se
#SBATCH --error /Midgard/home/%u/dino-finetune/logs/%J_slurm.err
#SBATCH --output /Midgard/home/%u/dino-finetune/logs/%J_slurm.out

echo "Starting job ${SLURM_JOB_ID} on ${SLURMD_NODENAME}"
nvidia-smi
. ~/miniconda3/etc/profile.d/conda.sh
pushd ~/dino-finetune
conda activate dino

python voc_training.py
    --txt-path
    --images-path
    --target-path