import wandb
wandb.init(project="dinoss_deneme", entity="dino-wsss-kth")
WANDB_API_KEY = "6e590174d1c8348e7c8d5fa11450551633dd06ef"
config = wandb.config

config.learning_rate = 0.0005
for i in range(5):
    wandb.log({"loss": i})


