#!/usr/bin/env bash
#SBATCH --mem 10GB
#SBATCH --gres gpu:3
#SBATCH --cpus-per-task 8
#SBATCH --constraint shelob
#SBATCH --time 48:00:00
#SBATCH --mail-type FAIL
#SBATCH --mail-user batuhany@kth.se
#SBATCH --error /Midgard/home/%u/dino/logs/%J_slurm.err
#SBATCH --output /Midgard/home/%u/dino/logs/%J_slurm.out

echo "Starting job ${SLURM_JOB_ID} on ${SLURMD_NODENAME}"
nvidia-smi
. ~/miniconda3/etc/profile.d/conda.sh
pushd ~/dino
conda activate dinoss

python -m torch.distributed.launch main_dino.py --data_path /local_storage/datasets/voc2012_for_dino \
    --output_dir /local_storage/users/batuhany/dino/checkpoints5 \
    --num_workers 4 \
    --batch_size_per_gpu 16 \
    --saveckp_freq 5 \
    --exp_name dinosstry5_lr:0.00005_shelob
    # --sstrain_checkpoint ~/local_storage/dino_chkp/dino_deitsmall8_pretrain_full_checkpoint/archive/data.pkl \