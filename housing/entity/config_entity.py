from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"]) 


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                  "transformed_train_dir",
                                                                  "transformed_test_dir",
                                                                  "preprocessed_object_file_path"])

ModelTrainConfig = namedtuple("ModelTrainConfig", ["trained_model_file_path","base_accuracy"])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])