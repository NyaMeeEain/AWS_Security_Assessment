# Metadata API With AWS CLI
By hijacking the temporary session used by the Lambda function, we should be able to obtain the same permissions that the Lambda function was assigned. The AWS CLI tool will
allow us to interact with the account resources directly. In order to configure it we will need to set the following environment variables locally. When using the extracted tokens it is essential to set the AWS_SESSION_TOKEN otherwise these keys and secrets will not be usable.

* export AWS_ACCESS_KEY_ID=​**ASIA5GTGMXOZQSGD67TY**
* export AWS_DEFAULT_REGION=​**btFjl90f5fXYnQSrtwLPOuNb7ynfcj16jFKz2kxt**
* export AWS_SECRET_ACCESS_KEY=​[AWS_SECRET_ACCESS_KEY]
* export AWS_SESSION_TOKEN=​[AWS_SESSION_TOKEN]
