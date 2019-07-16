import requests, json
from GrabShell.Headers import HeaderBrower


class KuGouMusicInterFace(HeaderBrower.Headers):

    # 获取搜索的歌手数据
    def search_singer_song(self):
        # https://searchrecommend.kugou.com/get/complex?word=%E5%91%A8%E6%9D%B0%E4%BC%A6

        response = requests.get(
            headers=self._headers_brower(),
            url='https://searchrecommend.kugou.com/get/complex',
            params={'word':'周杰伦'}
        )
        return response.json()

    # 网易云音乐搜索
    def search_singer_song_wangyi(self):
        response = requests.post(
            headers=self._headers_app(),
            url = 'https://music.163.com/eapi/artist/albums/6452',
            data={'params':'7142951783281A8922CE97B8E8A7F88B0F526C3686AFE96158F0189FF77D002C6A2F9B9D657E886B7D4B39E6F443897AF341F7CDA89260F3C037258FA4C60EBC041E8BBD216394CD331458FC20B72557C2DABEB6FDDDC8AB9DEAD1B749DE63FD90B02FE0DBD1E9D0659106F6D1912F74A6DBD8A8D1643C369873AFFEFDD4D9EFDE56E67A01899AA673012772F5BE78ABD4537FDEC5DE03A5FEB9AA6B8AC71425A5F75BAF89112CF4EA897CBCDDCCD5C6F3E5828413EB4E1E4617CF25DB2C920C96F1FC3E50BAA392A599057CA0E27AF984B7AD62E92C58CBB3AF15174DFED1C42E5E4F2983FE74A04E3331EFFC113B3AB60DEE8769A3C8B4492A352E7DCD303E6AC3EFD2229DF92E8A3FBFD4C2AFE765D91A76DCC9125C1F405EF6772EB04180613C0ED20FF20A773A804F94B3C0C9CAFF78875FA70423A8F042FCCB982B95DF073FB0EA146CECBD6763973CF85AE4D484C693D0AF6B68904442BADE2D79FCE4B17A4CE05615443444DF0DD7594F52579DD2D6E2AE936C90B4EE0E2D94B04A8B2FC874EC6111D90FC89EB32ABDD97E58'}
        )
        return response.text


if __name__ == '__main__':
    data = KuGouMusicInterFace().search_singer_song_wangyi()
    data_json = json.loads(data)
    albums_name_list = []
    for i in range(len(data_json['hotAlbums'])):
        albums_name = data_json['hotAlbums'][i]['name']
        albums_name_list.append(albums_name)
    print(albums_name_list)
    # data_json = json.dumps(data_json, sort_keys=True, indent=4).encode('utf-8').decode('unicode_escape')
    # print(data_json)