import boto3

client = boto3.client('ses')

response = client.send_email(
    Source='thegreencartkitchen@gmail.com',
    Destination={
        'ToAddresses': [
            'jeffmjack@gmail.com',
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
                'Data': 'hi, this is Jeff running a test for an email server',
                'Charset': 'ascii'
            },
            'Html': {
                'Data': 'looks like gmail or amazon defaults to using HTML in the message body',
                'Charset': 'ascii'
            }
        }
    },
    ReplyToAddresses=[
        'thegreencartkitchen@gmail.com',
    ],
    ReturnPath='jeffmjack@gmail.com',
    SourceArn='arn:aws:ses:us-east-1:005005808680:identity/thegreencartkitchen@gmail.com',
    ReturnPathArn='arn:aws:ses:us-east-1:005005808680:identity/jeffmjack@gmail.com'
)


