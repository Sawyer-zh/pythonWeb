from __future__ import absolute_import, unicode_literals

import os

from flask import Flask, request, abort, render_template
from wechatpy import parse_message, create_reply
from wechatpy.crypto import WeChatCrypto
from wechatpy.exceptions import InvalidAppIdException
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature

from robot import auto_chat_tuling
from handler_message import handler
# set token or get from environments
TOKEN = os.getenv('WECHAT_TOKEN', 'DailyFei')
EncodingAESKey = os.getenv('WECHAT_ENCODING_AES_KEY', 'fRUozyJdtyBPs90htH2Gew1vc9iwNkyIvteSg7IJveq')
AppId = os.getenv('WECHAT_APP_ID', 'wxf3d4a77f94efc7c3')

app = Flask(__name__)


@app.route('/')
def index():
    host = request.url_root
    return render_template('index.html', host=host)


@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echo_str = request.args.get('echostr', '')
    encrypt_type = request.args.get('encrypt_type', '')
    msg_signature = request.args.get('msg_signature', '')

    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)
    if request.method == 'GET':
        return echo_str
    else:
        crypto = WeChatCrypto(TOKEN, EncodingAESKey, AppId)
        try:
            msg = crypto.decrypt_message(
                request.data,
                msg_signature,
                timestamp,
                nonce
            )
        except (InvalidSignatureException, InvalidAppIdException):
            abort(403)
        # msg = parse_message(msg)

        reply = handler(msg)


        # if msg.type == 'text':
        #     replyString = auto_chat_tuling(msg.content)
        #     reply = create_reply(replyString, msg)
        # else:
        #     reply = create_reply('Sorry, can not handle this for now', msg)
        return crypto.encrypt_message(
            reply.render(),
            nonce,
            timestamp
        )


if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=False)
