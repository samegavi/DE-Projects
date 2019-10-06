import constants as cs
import  boto3
import  pandas as pd
import pyarrow
import  pandavro as pdx



def main():
    client = create_s3_client()
    download_dataset(client, cs.RAW_DATA_DIRECTORY)
    read_file = file_reader(cs.RAW_DATA_PATH)
    print(read_file.shape)
    transformed_data = domain_transformer(read_file)
    print(transformed_data.shape)
    save_transformed_data(transformed_data)
    upload_files(client, cs.S3_TRANSFORMED_DATA_BUCKET)
      
def create_s3_client():
    print('Creating s3 client')
    region = cs.S3_REGION
    return boto3.client('s3',region_name = region)

def download_dataset(client,path):
    print('Downloading dataset')
    try:
        client.download_file(cs.S3_RAW_DATA_BUCKET, cs.RAW_DATA_FILE_NAME, cs.RAW_DATA_DIRECTORY + cs.RAW_DATA_FILE_NAME)       
    except Exception as error:
        print(error)

def file_reader(path):
    try:
        return pd.read_csv(path)
    except Exception as error:
        print(error)  

def domain_transformer(data):
    print('Transforming data')
    domain_filter = data[cs.FILTER_COLUMN].notnull()
    #print(data[domain_filter].shape)
    return data[domain_filter]

def save_transformed_data(data):
    try:
        print('saving as Parquet')
        data.to_parquet(cs.TRANSFORMED_DATA_PATH_PARQUET)
        print('saving as AVRO')
        data.to_csv('filtered.csv')
        new_data = pd.read_csv('filtered.csv',keep_default_na=False)
        pdx.to_avro(cs.TRANSFORMED_DATA_PATH_AVRO, new_data)
        print('saving as JSON gzip')
        data.to_json(cs.TRANSFORMED_DATA_PATH_JSON,compression = 'gzip')
    except Exception as error:
        print(error)

def upload_files(client, bucket):
    try:
        print('Uploading transformed parquet data')
        client.upload_file(cs.TRANSFORMED_DATA_PATH_PARQUET, bucket,cs.S3_TRANSFORMED_DATA_PATH_PARQUET)
        print('Uploading transformed json data')
        client.upload_file(cs.TRANSFORMED_DATA_PATH_JSON, bucket,cs.S3_TRANSFORMED_DATA_PATH_JSON) 
        print('Uploading transformed avro data')
        client.upload_file(cs.TRANSFORMED_DATA_PATH_AVRO, bucket,cs.S3_TRANSFORMED_DATA_PATH_AVRO) 
        #client.upload_file()  
    except Exception as error:
        print(error)       


if __name__ == "__main__":
    main()




