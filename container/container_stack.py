from aws_cdk import (
    Stack,
    aws_ecr as _ecr,
    aws_ecs as _ecs,
    aws_ec2 as _ec2,
    aws_ecs_patterns as _ecs_patterns,
    core
)
from constructs import Construct

class ContainerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


# create ecr repository named factorial

        containerised_app_repository = _ecr.Repository(self, "factorial")

# create new vpc for ecs cluster
 
        containerised_app_vpc = _ec2.Vpc(self, "factorial-vpc", max_azs=2)

# create ecs cluster object named factorial   

        containerised_app_cluster = _ecs.Cluster(self, "factorial", vpc=containerised_app_vpc)

# create ecs application fargate service named factorial on the factorial cluster  with Elastic Load Balancer
 
        containerised_app_ecs_application = _ecs_patterns.ApplicationLoadBalancedFargateService(self, "factorial",
                                                           cluster=factorial,
                                                           cpu=256,
                                                           desired_count=2,
                                                           task_image_options=_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                               image=_ecs.ContainerImage.from_registry('amazon/amazon-ecs-sample')),
                                                           memory_limit_mib=512,
                                                           public_load_balancer=True)
        containerised_app_repository.grant_pull(containerised_app_ecs_application.task_definition.obtain_execution_role())
