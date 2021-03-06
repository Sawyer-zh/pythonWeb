import re

from net_ease import search_music
from official_account import get_recent
from robot import auto_chat_tuling
from wechatpy import parse_message, create_reply
from wechatpy.replies import TextReply, ArticlesReply
from zhihu import getRecommend
import random


def reply_text(msg):
    text = TextReply()
    text.content = msg
    return text


def reply_music(msg):
    '''
    使用的是ArticlesReply 因为连接大多失效
    :param msg:
    :return:
    '''
    # song = search_music(msg)
    # music = MusicReply()
    # music.title = song['name']
    # # music.description = song['album']['description']
    # music.description = '123'
    # music.music_url = song['mp3Url']
    # music.hq_music_url = song['mp3Url']
    # music.thumb_media_id = ''
    # print(music)

    r = search_music(msg)
    articlesReply = ArticlesReply()
    one = {'title': r['name'],
           'description': r['artists'][0]['name'],
           'image': r['artists'][0]['img1v1Url'],
           'url': ('http://music.163.com/m/song?id=%s&userid=368241565&from=message' % r['id'])
           }
    articlesReply.add_article(one)
    return articlesReply


def reply_article(msg):
    r = get_recent(msg)
    if r == '':
        reply = auto_chat_tuling(msg)
        return reply_text(reply)

    articleReply = ArticlesReply()
    one = {'title': r['wechat_name'],
           'description': r['introduction'],
           'image': r['headimage'],
           'url': r['profile_url']
           }
    articleReply.add_article(one)
    return articleReply

def reply_zhihu():
    articleReply = ArticlesReply()
    num = random.randint(1,10)
    results = getRecommend(str(num))
    for result in results:
        article = {}
        article['url'] = 'https://zhuanlan.zhihu.com' + result['url']
        article['image'] = result['image_url']
        article['title'] = result['title']
        article['description'] = result['author']['name']
        articleReply.add_article(result)
    return articleReply



def handler_text(msg):
    ret = re.search(r'歌曲[,: ，。](.*)$', msg)
    if ret:
        return reply_music(ret.group(1))

    ret = re.search(r'公众号[,: ，。](.*)$', msg)
    if ret:
        return reply_article(ret.group(1))

    if ret == '知乎':
        return reply_zhihu()

    reply = auto_chat_tuling(msg)
    return reply_text(reply)


def handler_event(msg):
    if msg == 'subscribe':
        reply = '''您好,欢迎关注我!
回复'歌曲 歌曲名'即可收听歌曲
回复'公众号 公众号名称'即可获得该公众号最近10条文章
回复其他内容暂时由聊天机器人回答'''
        return reply


def handler(msg):
    msg = parse_message(msg)
    if msg.type == 'text':
        reply = handler_text(msg.content)
        return create_reply(reply, msg)
    elif msg.type == 'event':
        reply = handler_event(msg.event)
        return create_reply(reply, msg)
    else:
        return create_reply('Sorry, I can not handle this for now', msg)


if __name__ == '__main__':
    handler_text('歌曲,给我一首')
    handler_text('公众号,雪球')
    handler_text('知乎')