from classifier import logger
from classifier.pipeline.stage_1_Data_ingestion import DataIngestionTrainingPipeline
from classifier.pipeline.stage_2_preparemodel import PrepareBaseModelTrainingPipeline
from classifier.pipeline.stage_3_model_training import ModelTrainingPipeline
from classifier.pipeline.stage_4_model_evaluation import EvaluationPipeline

import dagshub
dagshub.init(repo_owner='mekharemanan', repo_name='End-to-End-Pneumonia-detection-using-MLflow-DVC', mlflow=True)

STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Prepare Base Model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model= PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")        
    model_trainer = ModelTrainingPipeline()        
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    

STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e