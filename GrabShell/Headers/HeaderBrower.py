class Headers:

    def _headers_brower(self):
        data = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Content-Type': 'text/plain;charset=utf-8'
            # 'authority': 'searchrecommend.kugou.com'
        }
        return data

    def _headers_app(self):

        _data = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Origin': 'orpheus://orpheus',
            'Connection': 'keep-alive',
            'Cookie': 'osver=%E7%89%88%E6%9C%AC%2010.13.6%EF%BC%88%E7%89%88%E5%8F%B7%2017G65%EF%BC%89; deviceId=BA1B76ED-1B11-53C5-BBE5-5E0AD4EFB89F%7C74957D86-8799-4E9E-A814-47DECB32117A; os=osx; appver=1.5.9; MUSIC_A=fc8dc151475fc829b75a63a6c19d7c235e796338d701de406c272acb5fe5f50471ee71c648c0b52bb0905ad1102a74b25156ff0b547a5a47e4a5028e61bcff07c06a99cc1fc4b6f2f6f4703ad8bb3f76749d98e7ddba96c53a2f400d20c7c391025f6dd5aa5ebee8d3eede68823ad5e91bdbe48c2c785fb5; channel=netease;',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
        }
        return _data