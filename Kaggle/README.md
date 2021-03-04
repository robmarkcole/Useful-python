## Kaggle
* [Kaggle API](https://github.com/Kaggle/kaggle-api) -> download datasets etc
* Kaggle allows using google cloud services in kaggle notebooks - BigQuery, cloud storage and AutoMLad

## Secrets
```
import wandb
os.environ["WANDB_SILENT"] = "true"

from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
personal_key_for_api = user_secrets.get_secret("wandb-key")

! wandb login $personal_key_for_api
```