# learn-aws

LearningAWS

## Images

-   [microsoft-vscode-devcontainers](https://hub.docker.com/_/microsoft-vscode-devcontainers)
-   [customink / codespaces-features](https://github.com/customink/codespaces-features/tree/main/src)

## AWS

-   [Testing and debugging serverless applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html)

## Tutorials

-   [Develop Lambdas Locally in VS Code Using AWS SAM | AWS Lambda Tutorial](https://www.youtube.com/watch?v=mhdX4znMd2Q)
-   [Your First AWS Lambda Function In VS Code - 10 Minute Tutorial - For Beginners](https://www.youtube.com/watch?v=DA3hlLxTl-8)

## Description

### compose.yaml

The latest docker doesn't need version in compose.yaml, if you are running on older version, you need to add version: '3.8' to the top of the file.

This compose file will create a series of containers that will allow you to develop and test your lambda functions locally.

It will create a container with the following:

-   Development environment with VS Code
-   Localstack
-   DynamoDBLocal

The Devenvironment will using the [microsoft-vscode-devcontainers](https://hub.docker.com/_/microsoft-vscode-devcontainers) image, which is a preconfigured image with the following:

-   VS Code
-   Python 3.9
-   features/aws-cli:1
-   features/docker-in-docker:2
-   features/dotnet:1
-   features/sam-cli:

## Warning

For test purposes only, do not use this in production.

While testing a lambda function, it will build another docker image without current environment variables,
so, the lambda function will not have access to the environment variables,
You must hard code the environment variables in the lambda function.
