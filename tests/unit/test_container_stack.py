import aws_cdk as core
import aws_cdk.assertions as assertions
import json
import pytest

from container.container_stack import ContainerStack
from aws_cdk import core

def get_template():
    app = core.App()
    ContainerStack(app, "container")
    return json.dumps(app.synth().get_stack("container").template)


def test_ecr_repository_created():
    assert("AWS::ECR::Repository" in get_template())


def test_vpc_created():
    assert("AWS::EC2::VPC" in get_template())


def test_ecs_cluster_created():
    assert("AWS::ECS::Cluster" in get_template())


def test_ecs_service_created():
    assert("AWS::ECS::Service" in get_template())


def test_elb_created():
    assert("AWS::ElasticLoadBalancingV2::LoadBalancer" in get_template())
