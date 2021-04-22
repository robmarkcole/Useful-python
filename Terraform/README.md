## Terraform
* https://www.terraform.io/ & https://github.com/hashicorp/terraform
* Create a pipeline for provisioning Infrastructure as Code, provision and manage any cloud, infrastructure, or service -> create new resources, manage existing ones, and destroy those no longer needed.
* Reproducible production, staging, and development environments
* Combine multiple providers consistently
* human readable language called HCL (HashiCorp Configuration Language), similar to YAML, but not the same

## Examples
* Terraform module to deploy an Apache Airflow cluster on AWS, backed by RDS PostgreSQL for metadata, S3 for logs and SQS as message broker with CeleryExecutor -> [here](https://github.com/PowerDataHub/terraform-aws-airflow)