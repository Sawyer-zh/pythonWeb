import re

from net_ease import search_music
from wechatpy import parse_message, create_reply
from wechatpy.replies import MusicReply
from robot import auto_chat_tuling

def test():
    music = MusicReply()
    print(dir(music))


test()


def reply_music(msg):
    song = search_music(msg)
    music = MusicReply()
    music.title = song['name']
    music.description = song['album']['description']
    music.music_url = song['mp3Url']
    music.hq_music_url = song['mp3Url']
    music.thumb_media_id = '1'
    return create_reply(music)


def handler_text(msg):
    ret = re.search(r'歌曲,(.*)$', msg)
    if ret.group(1):
        return reply_music(ret.group(1))
    else:
        reply  = auto_chat_tuling(msg)
        return create_reply(reply)

def handler_event(msg):
    pass


def handler(msg):
    msg = parse_message(msg)
    if msg.type == 'text':
        return handler_text(msg)
    elif msg.type == 'event':
        handler_event(msg)
    else:
        return create_reply('Sorry, I can not handle this for now', msg)


if __name__ == '__main__':
    handler_text('歌曲,给我一首')
