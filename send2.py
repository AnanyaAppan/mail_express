import sendgrid
import os

def mailSend(mailId,emailList,sub,body):

    sg = sendgrid.SendGridAPIClient(apikey='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')
    for toMailId in emailList:
        data = {
        "personalizations": [
            {
            "to": [
                {
                "email": toMailId
                }
            ],
            "subject": sub
            }
        ],
        "from": {
            "email": mailId
        },
        "content": [
            {
            "type": "text/plain",
            "value": body
            }
        ]
        }
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)

