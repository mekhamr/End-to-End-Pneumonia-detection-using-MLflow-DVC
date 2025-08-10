# End-to-End-Pneumonia-detection-using-MLflow-DVC
# 1. Project Initialization & Settings
Configured config.yaml to define paths and global settings.
Specified hyperparameters (batch size, learning rate, epochs) in params.yaml.
Developed entity classes for structured configuration management.
Implemented a centralized Configuration Manager in src/config to load and manage all settings.
# 2. Component Development
Data Ingestion – Automated dataset loading and preprocessing of chest X-ray images.
Base Model Preparation – Initialized DenseNet121 architecture with predefined settings.
Model Training – Trained the model using hyperparameters from params.yaml.
Model Evaluation – Recorded metrics and stored artifacts using MLflow.
# 3. Pipeline Orchestration & Versioning
Integrated all components into a cohesive, automated execution pipeline.
Implemented main.py as the central pipeline trigger.
Defined and version-controlled pipeline stages in dvc.yaml for reproducibility.

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 541202655809.dkr.ecr.ap-south-1.amazonaws.com/pneumonia_chestxray

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo 

    ECR_REPOSITORY_NAME = 






