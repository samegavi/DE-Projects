RAW_DATA_FILE_NAME = 'free-7-million-company-dataset.zip'
RAW_DATA_PATH = 'raw-data/free-7-million-company-dataset.zip'
RAW_DATA_DIRECTORY = 'raw-data/'
TRANSFORMED_DATA_DIRECTORY = 'transformed-data/'
TRANSFORMED_DATA_PATH_PARQUET = TRANSFORMED_DATA_DIRECTORY + 'free-7-million-company-dataset.parquet'
TRANSFORMED_DATA_PATH_JSON = TRANSFORMED_DATA_DIRECTORY + 'free-7-million-company-dataset-json.gzip'
TRANSFORMED_DATA_PATH_AVRO = TRANSFORMED_DATA_DIRECTORY + 'free-7-million-company-dataset.avro'

#S3

S3_REGION = 'eu-west-1'
S3_RAW_DATA_BUCKET = 'blossom-data-engs'
S3_TRANSFORMED_DATA_BUCKET = 'blossom-data-eng-samuel-amegavi'
S3_TRANSFORMED_DATA_PATH_PARQUET = 'project1/free-7-million-company-dataset.parquet'
S3_TRANSFORMED_DATA_PATH_JSON = 'project1/free-7-million-company-dataset-json.gzip'
S3_TRANSFORMED_DATA_PATH_AVRO = 'project1/free-7-million-company-dataset.avro'
#Pandas

FILTER_COLUMN = 'domain'