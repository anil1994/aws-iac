import aws_cdk as core
import aws_cdk.assertions as assertions
import json
import pytest

from lambda.lambda_stack import LambdaStack
from aws_cdk import core



def get_template():
    app = core.App()
    LambdaStack(app, "lambda")
    return json.dumps(app.synth().get_stack("lambda").template)

def test_s3_bucket_created():
    assert("AWS::S3::Bucket" in get_template())


def test_lambda_created():
    assert("AWS::Lambda::Function" in get_template())

def test_dynamodb_created():
    assert("AWS::DynamoDB::Table" in get_template())
