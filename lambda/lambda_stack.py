from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_dynamodb as _dynamodb,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    core
)

from aws_cdk.aws_lambda_event_sources import S3EventSource

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
  
# create table object named employees on dynamodb
        serverless_db = _dynamodb.Table(self, id='dynamoTable', table_name='employees',
                                        partition_key=_dynamodb.Attribute(name='name', type=_dynamodb.AttributeType.STRING))

# create s3 bucket object named anildalkilic
        serverless_bucket = _s3.Bucket(
            self, id='s3bucket', bucket_name='anildalkilic')

# create lambda_function 

        serverless_lambda = _lambda.Function(self,
                                             id='csv-s3-trigger',
                                             runtime=_lambda.Runtime.PYTHON_3_8,
                                             handler='lambda_handler.lambda_handler',
                                             code=_lambda.Code.from_inline(
                                                 ' '),
                                             role=_iam.Role.from_role_arn(
                                                 self, id='lambda_role', 'arn:aws:iam::635719328626:role/service-role/csv-s3-trigger-role-uu2adzky')
                                             )

# trigger lambda function when csv is upload to s3

        serverless_lambda.add_event_source(S3EventSource(serverless_bucket,
                                                         events=[
                                                             _s3.EventType.OBJECT_CREATED]
                                                         ))
