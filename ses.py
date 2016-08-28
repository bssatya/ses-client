import boto3

client = boto3.client('ses')

response = client.send_email(
    Source='your_email@example.com',
    Destination={
        'ToAddresses': [
            'recipient_email@example.com',
        ],
#         'CcAddresses': [
#            'string',
#        ],
#        'BccAddresses': [
#            'string',
#        ]
    },
    Message={
        'Subject': {
            'Data': 'hi there from Amazon SES',
            'Charset': 'ascii'
        },
        'Body': {
            'Text': {
                'Data': 'hi, this is a test for a new SES emailing script - this is a plaintext message',
                'Charset': 'ascii'
            },
            'Html': {
                'Data': 'hi, this is a test for a new SES emailing script - this is an HTML message',
                'Charset': 'ascii'
            }
        }
    },
    ReplyToAddresses=[
        'your_email@example.com',
    ],
    ReturnPath='your_address@gmail.com',
    SourceArn='arn:aws:ses:us-east-1:005005808680:identity/confirmed_email_in_amazon@example.com',
    ReturnPathArn='arn:aws:ses:us-east-1:005005808680:identity/account_holder_email@example.com'
)


