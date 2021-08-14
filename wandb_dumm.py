import wandb
wandb.init(project="dinoss_deneme2", entity="dino-wsss-kth")
config = wandb.config

config.learning_rate = 0.0005
for i in range(5):
    wandb.log({"loss": i})


