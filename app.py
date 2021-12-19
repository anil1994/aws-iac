#!/usr/bin/env python3

import aws_cdk as cdk

from lambda.lambda_stack import LambdaStack
from container.container_stack import ContainerStack


app = cdk.App()
LambdaStack(app, "lambda")
ContainerStack(app, "container")

app.synth()
