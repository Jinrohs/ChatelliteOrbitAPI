# -*- coding: utf-8 -*-

import requests
import sys
import time


class TLE:
    """Two Line Element of satelites"""

    # TLE を更新する（Space-Track から取得し直す）周期
    # 単位は秒
    get_period = 30

    base_url = 'https://www.space-track.org/'
    login_url = base_url + 'ajaxauth/login'

    def __init__(self, username, password, satelite_num):
        self.login_data = {
            'identity': username,
            'password': password
        }
        self.satelite_num = satelite_num
        self.update_time = 0
        self.tle = self.get_tle()

    def get_tle(self):
        """get TLE from Space-Track"""
        s = requests.Session()
        # log in Space-Track
        print s.post(self.login_url, data=self.login_data)
        # get TLE with object No.
        res = s.get(
            self.base_url +
            "basicspacedata/query/class/tle_latest/ORDINAL/1/NORAD_CAT_ID/" +
            "{0}/orderby/TLE_LINE1 ASC/format/json".
            format(self.satelite_num)
        ).json()[0]
        self.update_time = time.time()
        return res
