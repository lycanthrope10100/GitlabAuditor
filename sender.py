import sys
from datetime import datetime
from dateutil import tz
from json import dumps
from httplib2 import Http
user = str(sys.argv[1])
project = str(sys.argv[2])
remote_ip = str(sys.argv[3])
time = str(sys.argv[4])
type_ = 'card'

def webhook(user, project, remote_ip, time):
    url = '<your_webhook_url>'
    if type_ == 'json':
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        message = {
            'text': '*Clone Alert!*\n'+payload
        }
    elif type_ == 'card':
        message_headers = {'Content-Type': 'image/jpg'}
        content = '<your_gitlab_url>/'+project
        message = {
            "cards": [
                {
                    "sections": [
                        {
                            "widgets": [
                                {
                                    "keyValue": {
                                        "topLabel": time,
                                        "content": user,
                                        "contentMultiline": "false",
                                        "bottomLabel": remote_ip,
                                        "icon": "PERSON",
                                        "button": {
                                            "textButton": {
                                                "text": "GO",
                                                "onClick": {
                                                    "openLink": {
                                                        "url": content
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    else:
        message_headers = {'Content-Type: text/html; charset=UTF-8'}
        message = 'message'
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(message),
    )
    print(response)

if __name__ == '__main__':
        utc_tz= tz.gettz('UTC')
        india_tz= tz.gettz('Asia/Kolkata')
        date_string=time
        utc = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
        utc = utc.replace(tzinfo=utc_tz)
        india_time_with_offset = utc.astimezone(india_tz)
        india_time_without_offset = india_time_with_offset.replace(tzinfo=None)
        webhook(user, project, remote_ip, str(india_time_without_offset))
