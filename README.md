# End-to-End-Pneumonia-detection-using-MLflow-DVC
This project detects pneumonia from chest X-ray images using a DenseNet121 deep learning model, integrated with MLflow for experiment tracking, DVC for dataset versioning, and a CI/CD pipeline for automated deployment on AWS
# Architecture

 <img width="500" height="395" alt="Screenshot (193)" src="https://github.com/user-attachments/assets/b3be3b95-d680-4e12-a38f-7b449beb8892" />


# 1. Project Initialization & Settings
* Configured config.yaml to define paths and global settings.
* Specified hyperparameters (batch size, learning rate, epochs) in params.yaml.
* Developed entity classes for structured configuration management.
* Implemented a centralized Configuration Manager in src/config to load and manage all settings.
  
* Core functionality is implemented through modular components
	* Data Ingestion – Automated dataset loading and preprocessing of chest X-ray images.
	* Base Model Preparation – Initialized DenseNet121 architecture with predefined settings.
	* Model Training – Trained the model using hyperparameters from params.yaml.
	* Model Evaluation – Recorded metrics and stored artifacts using MLflow.
    * Prediction Pipeline – Provides an interface for running model predictions on new images.

* Pipeline Orchestration & Versioning
	* Integrated all components into a automated execution pipeline.
	* Implemented main.py as the central pipeline trigger.
	* Defined and version-controlled pipeline stages in dvc.yaml for reproducibility.

# 2. Model Development 
* Leveraged DenseNet121 pre-trained on ImageNet for robust feature extraction from chest X-ray images.
* Customized the architecture by removing the original classification head and adding layers for binary pneumonia detection.
* Enhanced performance through fine-tuning of the upper DenseNet layers.
* Evaluated performance using Precision, Recall, and Accuracy metrics.

# 3. Model Experimentation and Tracking with MLflow
* Used MLflow with DagsHub integration to log parameters, metrics, confusion matrices, and model artifacts.
* Enabled model versioning, remote storage, and experiment comparison through mlflow ui.
  
# 4.Data Version Control (DVC) Integration
* Implemented DVC to track and version the chest X-ray dataset, ensuring reproducibility across experiments.
* Stored large data files in remote storage while keeping lightweight metadata in Git for easy collaboration.
* Defined pipeline stages in dvc.yaml to automate steps like data ingestion, model preparation, training, and evaluation.
* Enabled rollback to previous dataset or model versions for experiment comparison and debugging.
  
# 5. AWS-CICD-Deployment-with-Github-Actions
* Setup AWS Infrastructure:
	* Create an IAM user with permissions to manage EC2 and ECR (AmazonEC2FullAccess + AmazonEC2ContainerRegistryFullAccess).
	* Create an ECR repository to store Docker container images.
	* Launch an EC2 instance (Ubuntu) configured with security groups that allow SSH and Docker operations.
* Build & Push Docker Image:
	* On your local machine or GitHub Actions runner, build a Docker image from your application code.
	* Tag the Docker image with the ECR repository URI.
	* Authenticate Docker client with AWS ECR using IAM credentials.
	* Push the Docker image to the ECR repository.
* Deploy Docker Container on EC2:
	* SSH into the EC2 instance.
	* Pull the latest Docker image from ECR.
	* Run the Docker container on EC2.
* GitHub Actions Integration:
	* Configure the EC2 instance as a self-hosted GitHub Actions runner to allow running workflows directly on the instance.
	* Store AWS credentials and ECR/repo information as GitHub Secrets for secure access within workflows.
	* Create GitHub Actions workflows to automate the build, push, and deploy steps whenever code is pushed or merged into the repository.
 * How the CI/CD Pipeline Works
	* When you push code to GitHub, GitHub Actions triggers the pipeline workflow.
	* The workflow:
		* Builds the Docker image from your updated code.
		* Authenticates and pushes the Docker image to the AWS ECR repository.
	* On the EC2 instance, you can automate or manually:
		* Pull the new Docker image from ECR.
		* Restart or launch the container with the updated image.
  # 6. Pneumonia Detection Web Application 
  * Developed a Flask-based web application enabling user interaction through an intuitive interface.
  * The application supports uploading chest X-ray images to classify cases as normal or pneumonia using a pre-trained DenseNet121 model.
  * Predictions are served via a RESTful API integrated with an HTML front-end.
  * During development, the application runs locally using app.py and is configured to operate on a custom port within an AWS environment following CI/CD deployment.
  
 <img width="500" height="946" alt="Screenshot (186)" src="https://github.com/user-attachments/assets/71223176-e70d-4410-9e70-5795837e0f49" />




