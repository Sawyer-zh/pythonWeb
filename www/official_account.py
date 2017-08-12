import wechatsogou

api = wechatsogou.WechatSogouAPI()


def get_recent(name):
    searchResult = api.search_gzh(name, 1)
    for result in searchResult:
        if result['wechat_name'] == name:
            accurate = api.get_gzh_info(result['wechat_id'])
            return accurate
        else:
            return ''


if __name__ == '__main__':
    get_recent('飞飞日常')
