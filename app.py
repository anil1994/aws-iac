#!/usr/bin/env python3

from aws_cdk import core
from lambda_stack.lambda_stack import LambdaStack
from container_stack.container_stack import ContainerStack

app = cdk.App()
LambdaStack(app, "lambda")
ContainerStack(app, "container")

app.synth()
