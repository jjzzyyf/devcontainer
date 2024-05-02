import boto3
import os


class Boto3Client:
    def UseEnvironmentCredentials(self):
        self._aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID", "foo")
        self._aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", "bar")

        return self

    def UseCustomCredentials(
        self, region_name, endpoint_url, aws_access_key_id, aws_secret_access_key
    ):
        self._region_name = region_name
        self._endpoint_url = endpoint_url
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key

        return self

    def UseLocalDynamoDB(self):
        self._service = "dynamodb"
        # self._region_name = os.getenv("AWS_REGION", "localhost")
        # self._endpoint = os.getenv("DYNAMODB_ENDPOINT", "http://dynamodb:8000")
        self._region_name = "localhost"
        self._endpoint_url = "http://dynamodb:8000"

        return self

    def UseLocalSQS(self):
        self._service = "sqs"
        self._region_name = os.getenv("AWS_REGION", "localhost")
        self._endpoint_url = os.getenv("AWS_ENDPOINT", "http://localstack:4566")

        return self

    def CreateClient(self):

        return boto3.client(
            self._service,
            region_name=self._region_name,
            endpoint_url=self._endpoint_url,
            aws_access_key_id=self._aws_access_key_id,
            aws_secret_access_key=self._aws_secret_access_key,
        )

    def CreateResource(self):

        return boto3.resource(
            self._service,
            region_name=self._region_name,
            endpoint_url=self._endpoint_url,
            aws_access_key_id=self._aws_access_key_id,
            aws_secret_access_key=self._aws_secret_access_key,
        )
