import base64
import time
import logging
import json
from apiclient import errors
from docopt import docopt
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

logger = logging.getLogger(__name__)

from gmail_credential import get_credential

def list_labels(service, user_id):
    """
    label のリストを取得する
    """
    labels = []
    response = service.users().labels().list(userId=user_id).execute()
    return response["labels"]

def decode_base64url_data(data):
    """
    base64url のデコード
    """
    decoded_bytes = base64.urlsafe_b64decode(data)
    decoded_message = decoded_bytes.decode("UTF-8")
    return decoded_message


def list_message(service, query, user_id, count):
    messages = []
    try:
        message_ids = (
            service.users()
            .messages()
            .list(userId=user_id, maxResults=count, q=query)
            .execute()
        )

        if message_ids["resultSizeEstimate"] == 0:
            logger.warning("no result data!")
            return []

        # message id を元に、message の内容を確認
        for message_id in message_ids["messages"]:
            message_detail = (
                service.users()
                .messages()
                .get(userId="me", id=message_id["id"])
                .execute()
            )
            print (message_detail)

            message = {}
            message["id"] = message_id["id"]

            #partsがない場合
            if 'parts' not in message_detail['payload']:
                print("ifに入った")
                message["body"] = decode_base64url_data(
                    message_detail["payload"]["body"]["data"]
                )
            # 単純なテキストメールの場合
            elif 'data' in message_detail['payload']['body']:
                message["body"] = decode_base64url_data(
                    message_detail["payload"]["body"]["data"]
                    )
            # html メールの場合、plain/text のパートを使う
            else:
                parts = message_detail['payload']['parts']
                parts = [part for part in parts if part['mimeType'] == 'text/plain']
                message["body"] = decode_base64url_data(
                    parts[0]['body']['data']
                    )
            # payload.headers[name: "Subject"]
            message["subject"] = [
                header["value"]
                for header in message_detail["payload"]["headers"]
                if header["name"] == "Subject"
            ][0]
            # payload.headers[name: "From"]
            message["from"] = [
                header["value"]
                for header in message_detail["payload"]["headers"]
                if header["name"] == "From"
            ][0]
            logger.info(message_detail["snippet"])
            messages.append(message)
    
        item = next((m for m in message_detail['payload']['headers'] if m['name'] == 'Subject'), None)
        if item['value'] == "map":
            print("Subject:" + item['value'])

            if 'parts' not in message_detail['payload']:
                
                body = decode_base64url_data(message_detail['payload']['body']['data'])
            else:
                body = decode_base64url_data(message_detail['payload']['parts'][0]['body']['data'])

        print(body)
        return messages

    except errors.HttpError as error:
        print("An error occurred: %s" % error)


   

       


def remove_labels(service, user_id, messages, remove_labels):
    """
    ラベルを削除する。既読にするために利用(is:unread ラベルを削除すると既読になる）
    """
    message_ids = [message["id"] for message in messages]
    labels_mod = {
        "ids": message_ids,
        "removeLabelIds": remove_labels,
        "addLabelIds": [],
    }
    # import pdb;pdb.set_trace()
    try:
        message_ids = (
            service.users()
            .messages()
            .batchModify(userId=user_id, body=labels_mod)
            .execute()
        )
    except errors.HttpError as error:
        print("An error occurred: %s" % error)

# メイン処理
def main(query = "is:unread" , count=4):
    creds = get_credential()
    service = build("gmail", "v1", credentials=creds, cache_discovery=False)
    # メール一覧 [{'body': 'xxx', 'subject': 'xxx', 'from': 'xxx'},]

    labels = list_labels(service, "me")
    target_label_ids = [label["id"] for label in labels]
    # メール一覧 [{'body': 'xxx', 'subject': 'xxx', 'from': 'xxx'},]
    messages = list_message(service, query, "me",count)
    # unread label
    unread_label_ids = [label["id"] for label in labels if label["name"] == "UNREAD"]
    # remove labels form messages
    remove_labels(service, "me", messages, remove_labels=unread_label_ids)
    logger.info(json.dumps(messages, ensure_ascii=False))
    if messages:
        return json.dumps(messages, ensure_ascii=False)
    else:
        return None


# プログラム実行部分
if __name__ == "__main__":
    # arguments = docopt(__doc__, version="0.1")
    # query = arguments["<query>"]
    # count = arguments["<count>"]
    logging.basicConfig(level=logging.DEBUG)
    #while True:
    messages_ = main()
    print(messages_)
        #time.sleep(2)