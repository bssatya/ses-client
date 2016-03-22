# AWS SDK for Python SES Emailer

A simple Python application illustrating usage of the AWS SDK for Python (also
referred to as `boto3`).

## Requirements

This sample project depends on `boto3`, the AWS SDK for Python, and requires
Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install `boto3` using pip:

Boto3 is already included in the repo; however it was set up via python's virtualenv
for system-wide package management; so in order to access the package you must run
  `$PROJECT_ROOT/source venv/bin/activate` to setup the correct python virtual environment.

## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by creating a file named "credentials" at ~/.aws/ 
(`C:\Users\USER_NAME\.aws\` for Windows users) and saving the following lines in the file:

    [default]
    region = your-region <e.g. aws-east-1>
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>
    

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys. For more information on configuring `boto3`,
check out the Quickstart section in the [developer guide](https://boto3.readthedocs.org/en/latest/guide/quickstart.html).

## Running the SES sample

This sample application sends a simple email from one verified address to another (so you can use it while still in the sandbox).
All you need to do is update the `ses.py` file for the correct email addresses, and make sure your ~/.aws/credentials file has the 
correct access keys (note my access keys are not included in this repo)

    `$PROJECT_ROOT/source venv/bin/activate
    python ses.py`

You need to make sure the credentials you're using have the correct permissions to access the Amazon SES
service. If you run into 'Access Denied' errors while running this sample, please follow the steps below.

1. Log into the [AWS IAM Console](https://console.aws.amazon.com/iam/home)
2. Navigate to the Users page.
3. Find the AWS IAM user whose credentials you're using.
4. Under the 'Permissions' section, attach the policy called 'AmazonS3FullAccess'
5. Re-run the sample. Now your user should have the right permissions to run the sample.


## License

This sample application is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

