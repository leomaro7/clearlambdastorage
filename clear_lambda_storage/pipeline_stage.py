from constructs import Construct
from aws_cdk import (
    Stage
)
from .clear_lambda_storage_stack import ClearLambdaStorageStack

class ClearLambdaStoragePipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = ClearLambdaStorageStack(self, 'clearlambdastoragestack')