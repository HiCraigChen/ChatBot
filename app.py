from flask import Flask
from flask import abort
from flask import request
import requests
app = Flask(__name__)

PAGE_TOKEN = "<Your own PAGE_TOKEN>"
BOT_TOKEN = "<Your own BOT_TOKEN>"

@app.route("/", methods=['GET'])
def version():
    if request.method == 'GET':
        return "Connected"
    else:
        abort(404)
        

@app.route("/fbCallback", methods=['GET', 'POST'])
def fb_cb_handler():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        if token == BOT_TOKEN:
            return request.args.get('hub.challenge')
        else:
            abort(403)
    elif request.method == 'POST':
        return fb_post_handler(request)
    else:
        abort(405) 


FB_MESSENGER_URI = "https://graph.facebook.com/v2.6/me/messages?access_token=" + PAGE_TOKEN

def send_template_message(user_id, elements):
    data = {
        "recipient":{
            "id": user_id
        },
        "message":{
            "attachment": {
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements": elements
                }
            }
        }
    }

    r = requests.post(FB_MESSENGER_URI, json=data)
    if r.status_code != requests.codes.ok:
        print(r.content)

def send_text(reply_token, text, answers):
    data = {
        "recipient": {"id": reply_token},
        "message": {"text": text}
    }
    if answers:
        data["message"]["quick_replies"] = answers
    r = requests.post(FB_MESSENGER_URI, json=data)
    if r.status_code != requests.codes.ok:
        print(r.content)

def fb_post_handler(req):
    print(req.get_data())
    resp_body = req.get_json()

    for entry in resp_body["entry"]:
        for msg in entry["messaging"]:
            sender = msg['sender']['id']
            if 'message' in msg:
                if msg['message'].get('is_echo'):
                    return ""
                if 'text' not in msg['message']:
                    return ""
                if 'quick_reply' in msg['message']:
                    reply = msg["message"]["quick_reply"]
                    if reply['payload'] == "QUERY_CURRENCY":
                        send_text(sender, "This function is not worked yet.", None)
                    elif reply['payload'] == "CANCEL":
                        send_text(sender, "No problem.", None)
                    return ""
                text = msg['message']['text']
                send_text(sender, text, None)
            elif 'postback' in msg:
                if msg['postback']['payload'] == "GET_STARTED":
                    send_text(sender, 'welcome', None)
                elif msg['postback']['payload'] == "HAHAHA":
                    send_text(sender, 'hahaha!', None)
    return ""



if __name__ == "__main__":
    app.run(port=11123)