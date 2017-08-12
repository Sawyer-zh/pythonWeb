import requests

cookies = {'appver': '1.5.2'}
headers = {'referer': 'http://music.163.com'}


def get_music(song):
    musicUrl = 'http://music.163.com/api/album/%d/' % song['album']['id']
    r = requests.get(musicUrl, headers=headers, cookies=cookies)
    if r.json()['code'] == 200:
        for single in r.json()['album']['songs']:
            if single['id'] == song['id']:
                return single


def search_music(kws):
    url = 'http://music.163.com/api/search/get/'
    payload = {'s': kws, 'limit': '1', 'type': '1', 'offset': 0}
    r = requests.post(url, cookies=cookies, headers=headers, data=payload)
    if r.json()['code'] == 200:
        return  r.json()['result']['songs'][0]



if __name__ == '__main__':
    r =search_music('道姑朋友')
    print(r)
    print(r['id'])
    print(r['name'])
    print(r['artists'][0]['name'])
    print(r['artists'][0]['img1v1Url'])
    print(r)

        # {
        #     'code': 200,
        #     'album': {
        #         'songs': [
        #             {
        #                 'starred': False,
        #                 'popularity': 100.0,
        #                 'starredNum': 0,
        #                 'playedNum': 0,
        #                 'dayPlays': 0,
        #                 'hearTime': 0,
        #                 'mp3Url': 'http: //m2.music.126.net/Id5dzCSo5CxXGMCd7ur2TQ==/7942872001389925.mp3',
        #                 'rtUrls': None,
        #                 'status': 0,
        #                 'audition': None,
        #                 'ringtone': None,
        #                 'disc': '1',
        #                 'no': 1,
        #                 'commentThreadId': 'R_SO_4_34497631',
        #                 'fee': 0,
        #                 'copyFrom': '',
        #                 'mMusic': {
        #                     'playTime': 299598,
        #                     'volumeDelta': 0.0,
        #                     'dfsId': 7751556977066285,
        #                     'bitrate': 160000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871185,
        #                     'size': 5993056,
        #                     'extension': 'mp3'
        #                 },
        #                 'lMusic': {
        #                     'playTime': 299598,
        #                     'volumeDelta': -0.000265076,
        #                     'dfsId': 7942872001389925,
        #                     'bitrate': 96000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871186,
        #                     'size': 3595851,
        #                     'extension': 'mp3'
        #                 },
        #                 'hMusic': {
        #                     'playTime': 299598,
        #                     'volumeDelta': 0.0220296,
        #                     'dfsId': 7986852466492043,
        #                     'bitrate': 320000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871184,
        #                     'size': 11986067,
        #                     'extension': 'mp3'
        #                 },
        #                 'score': 100,
        #                 'album': {
        #                     'songs': [

        #                     ],
        #                     'paid': False,
        #                     'onSale': False,
        #                     'status': 0,
        #                     'tags': '',
        #                     'publishTime': 1441555200007,
        #                     'commentThreadId': 'R_AL_3_3286247',
        #                     'picId': 3342515349077641,
        #                     'blurPicUrl': 'http: //p4.music.126.net/cs5o_o6375tXrFcCHk7XZA==/3342515349077641.jpg',
        #                     'companyId': 0,
        #                     'pic': 3342515349077641,
        #                     'picUrl': 'http: //p3.music.126.net/cs5o_o6375tXrFcCHk7XZA==/3342515349077641.jpg',
        #                     'artist': {
        #                         'img1v1Id': 18686200114669622,
        #                         'topicPerson': 0,
        #                         'musicSize': 0,
        #                         'picId': 0,
        #                         'trans': '',
        #                         'picUrl': 'http: //p4.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
        #                         'briefDesc': '',
        #                         'albumSize': 0,
        #                         'img1v1Url': 'http: //p4.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #                         'alias': [

        #                         ],
        #                         'name': '',
        #                         'id': 0,
        #                         'img1v1Id_str': '18686200114669622'
        #                     },
        #                     'copyrightId': 0,
        #                     'description': '',
        #                     'subType': None,
        #                     'artists': [
        #                         {
        #                             'img1v1Id': 18686200114669622,
        #                             'topicPerson': 0,
        #                             'musicSize': 0,
        #                             'picId': 0,
        #                             'trans': '',
        #                             'picUrl': 'http: //p3.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
        #                             'briefDesc': '',
        #                             'albumSize': 0,
        #                             'img1v1Url': 'http: //p3.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #                             'alias': [

        #                             ],
        #                             'name': '苏琛',
        #                             'id': 1146106,
        #                             'img1v1Id_str': '18686200114669622'
        #                         }
        #                     ],
        #                     'company': '',
        #                     'briefDesc': '',
        #                     'alias': [

        #                     ],
        #                     'name': '好说好散',
        #                     'id': 3286247,
        #                     'type': None,
        #                     'size': 2
        #                 },
        #                 'copyrightId': 0,
        #                 'crbt': None,
        #                 'bMusic': {
        #                     'playTime': 299598,
        #                     'volumeDelta': -0.000265076,
        #                     'dfsId': 7942872001389925,
        #                     'bitrate': 96000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871186,
        #                     'size': 3595851,
        #                     'extension': 'mp3'
        #                 },
        #                 'rtUrl': None,
        #                 'position': 1,
        #                 'duration': 299598,
        #                 'artists': [
        #                     {
        #                         'img1v1Id': 18686200114669622,
        #                         'topicPerson': 0,
        #                         'musicSize': 0,
        #                         'picId': 0,
        #                         'trans': '',
        #                         'picUrl': 'http: //p3.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
        #                         'briefDesc': '',
        #                         'albumSize': 0,
        #                         'img1v1Url': 'http: //p4.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #                         'alias': [

        #                         ],
        #                         'name': '苏琛',
        #                         'id': 1146106,
        #                         'img1v1Id_str': '18686200114669622'
        #                     }
        #                 ],
        #                 'mvid': 0,
        #                 'ftype': 0,
        #                 'rtype': 0,
        #                 'rurl': None,
        #                 'alias': [

        #                 ],
        #                 'name': '好说好散',
        #                 'id': 34497631
        #             },
        #             {
        #                 'starred': False,
        #                 'popularity': 100.0,
        #                 'starredNum': 0,
        #                 'playedNum': 0,
        #                 'dayPlays': 0,
        #                 'hearTime': 0,
        #                 'mp3Url': 'http: //m2.music.126.net/bPBbAGKtTZXdNX9NzHlvew==/7827423279373369.mp3',
        #                 'rtUrls': None,
        #                 'status': 0,
        #                 'audition': None,
        #                 'ringtone': None,
        #                 'disc': '1',
        #                 'no': 2,
        #                 'commentThreadId': 'R_SO_4_34497630',
        #                 'fee': 0,
        #                 'copyFrom': '',
        #                 'mMusic': {
        #                     'playTime': 230974,
        #                     'volumeDelta': 0.126297,
        #                     'dfsId': 3301833418849552,
        #                     'bitrate': 160000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871182,
        #                     'size': 4620582,
        #                     'extension': 'mp3'
        #                 },
        #                 'lMusic': {
        #                     'playTime': 230974,
        #                     'volumeDelta': -0.000265076,
        #                     'dfsId': 7827423279373369,
        #                     'bitrate': 96000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871183,
        #                     'size': 2772367,
        #                     'extension': 'mp3'
        #                 },
        #                 'hMusic': {
        #                     'playTime': 230974,
        #                     'volumeDelta': -0.000265076,
        #                     'dfsId': 8003345140903227,
        #                     'bitrate': 320000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871181,
        #                     'size': 9241120,
        #                     'extension': 'mp3'
        #                 },
        #                 'score': 100,
        #                 'album': {
        #                     'songs': [

        #                     ],
        #                     'paid': False,
        #                     'onSale': False,
        #                     'status': 0,
        #                     'tags': '',
        #                     'publishTime': 1441555200007,
        #                     'commentThreadId': 'R_AL_3_3286247',
        #                     'picId': 3342515349077641,
        #                     'blurPicUrl': 'http: //p4.music.126.net/cs5o_o6375tXrFcCHk7XZA==/3342515349077641.jpg',
        #                     'companyId': 0,
        #                     'pic': 3342515349077641,
        #                     'picUrl': 'http: //p3.music.126.net/cs5o_o6375tXrFcCHk7XZA==/3342515349077641.jpg',
        #                     'artist': {
        #                         'img1v1Id': 18686200114669622,
        #                         'topicPerson': 0,
        #                         'musicSize': 0,
        #                         'picId': 0,
        #                         'trans': '',
        #                         'picUrl': 'http: //p4.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
        #                         'briefDesc': '',
        #                         'albumSize': 0,
        #                         'img1v1Url': 'http: //p3.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #                         'alias': [

        #                         ],
        #                         'name': '',
        #                         'id': 0,
        #                         'img1v1Id_str': '18686200114669622'
        #                     },
        #                     'copyrightId': 0,
        #                     'description': '',
        #                     'subType': None,
        #                     'artists': [
        #                         {
        #                             'img1v1Id': 18686200114669622,
        #                             'topicPerson': 0,
        #                             'musicSize': 0,
        #                             'picId': 0,
        #                             'trans': '',
        #                             'picUrl': 'http: //p4.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
        #                             'briefDesc': '',
        #                             'albumSize': 0,
        #                             'img1v1Url': 'http: //p4.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #                             'alias': [

        #                             ],
        #                             'name': '苏琛',
        #                             'id': 1146106,
        #                             'img1v1Id_str': '18686200114669622'
        #                         }
        #                     ],
        #                     'company': '',
        #                     'briefDesc': '',
        #                     'alias': [

        #                     ],
        #                     'name': '好说好散',
        #                     'id': 3286247,
        #                     'type': None,
        #                     'size': 2
        #                 },
        #                 'copyrightId': 0,
        #                 'crbt': None,
        #                 'bMusic': {
        #                     'playTime': 230974,
        #                     'volumeDelta': -0.000265076,
        #                     'dfsId': 7827423279373369,
        #                     'bitrate': 96000,
        #                     'sr': 44100,
        #                     'name': None,
        #                     'id': 103871183,
        #                     'size': 2772367,
        #                     'extension': 'mp3'
        #                 },
        #                 'rtUrl': None,
        #                 'position': 1,
        #                 'duration': 230974,
        #                 'artists': [
        #                     {
        #                         'img1v1Id': 18686200114669622,
        #                         'topicPerson': 0,
        #                         'musicSize': 0,
        #                         'picId': 0,
        #                         'trans': '',
        #                         'picUrl': 'http: //p4.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
        #                         'briefDesc': '',
        #                         'albumSize': 0,
        #                         'img1v1Url': 'http: //p4.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #                         'alias': [

        #                         ],
        #                         'name': '苏琛',
        #                         'id': 1146106,
        #                         'img1v1Id_str': '18686200114669622'
        #                     }
        #                 ],
        #                 'mvid': 0,
        #                 'ftype': 0,
        #                 'rtype': 0,
        #                 'rurl': None,
        #                 'alias': [

        #                 ],
        #                 'name': '最后一首情歌',
        #                 'id': 34497630
        #             }
        #         ],
        #         'paid': False,
        #         'onSale': False,
        #         'status': 0,
        #         'tags': '',
        #         'publishTime': 1441555200007,
        #         'commentThreadId': 'R_AL_3_3286247',
        #         'picId': 3342515349077641,
        #         'blurPicUrl': 'http: //p4.music.126.net/cs5o_o6375tXrFcCHk7XZA==/3342515349077641.jpg',
        #         'companyId': 0,
        #         'pic': 3342515349077641,
        #         'picUrl': 'http: //p3.music.126.net/cs5o_o6375tXrFcCHk7XZA==/3342515349077641.jpg',
        #         'artist': {
        #             'img1v1Id': 18686200114669622,
        #             'topicPerson': 0,
        #             'musicSize': 32,
        #             'picId': 8002245629271733,
        #             'trans': '',
        #             'picUrl': 'http: //p3.music.126.net/X3QUm9VZxOzv4tanps40uQ==/8002245629271733.jpg',
        #             'briefDesc': '',
        #             'albumSize': 21,
        #             'img1v1Url': 'http: //p3.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #             'alias': [

        #             ],
        #             'name': '苏琛',
        #             'id': 1146106,
        #             'img1v1Id_str': '18686200114669622'
        #         },
        #         'copyrightId': 0,
        #         'description': '',
        #         'subType': None,
        #         'artists': [
        #             {
        #                 'img1v1Id': 18686200114669622,
        #                 'topicPerson': 0,
        #                 'musicSize': 0,
        #                 'picId': 0,
        #                 'trans': '',
        #                 'picUrl': 'http: //p3.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
        #                 'briefDesc': '',
        #                 'albumSize': 0,
        #                 'img1v1Url': 'http: //p4.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
        #                 'alias': [

        #                 ],
        #                 'name': '苏琛',
        #                 'id': 1146106,
        #                 'img1v1Id_str': '18686200114669622'
        #             }
        #         ],
        #         'company': '',
        #         'briefDesc': '',
        #         'alias': [

        #         ],
        #         'name': '好说好散',
        #         'id': 3286247,
        #         'type': None,
        #         'size': 2,
        #         'info': {
        #             'latestLikedUsers': None,
        #             'liked': False,
        #             'comments': None,
        #             'resourceType': 3,
        #             'resourceId': 3286247,
        #             'commentCount': 43,
        #             'likedCount': 0,
        #             'shareCount': 12,
        #             'threadId': 'R_AL_3_3286247'
        #         }
        #     }
        # }
