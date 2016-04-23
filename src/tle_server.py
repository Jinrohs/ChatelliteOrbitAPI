# -*- coding: utf-8 -*-

import requests
import sys
import time
from flask import Flask, jsonify, request

from tle_calculator import TLECalculator

app = Flask(__name__)


# user name (email address)
username = sys.argv[1]
# password
password = sys.argv[2]
# NORAD の衛星カタログ番号
"""
- 29479: ひので
- 33492: いぶき
- 25544: ISS
- 39084: LANDSAT
"""
satelite_nums = ["29479", "33492", "39084"]

login_data = {'identity': username, 'password': password}
base_url = 'https://www.space-track.org/'
login_url = base_url + 'ajaxauth/login'

# TLE を更新する（Space-Track から取得し直す）周期
# 単位は秒
tle_get_period_sec = 30

tles = []
tle_get_time = 0


@app.route('/a')
def return_tle():
    global tle_get_time, tles
    time_now = time.time()
    if time_now - tle_get_time > tle_get_period_sec:
        tles = update_tles()
        tle_get_time = time_now

    # tmp
    print tle_get_time
    return jsonify(ResultSet=tles)


@app.route('/lat_lng_alt')
def return_latitude_longitude_altitude():
    """
    指定された時刻、カタログ ID の衛星の現在位置を返す
    - 高度 [km]
    - 緯度 [deg]
    - 経度 [deg]
    """
    global tles
    try:
        unixtime = request.args.get("time", type=int)
        s_ids = request.args.get("ids", default="all")
    except Exception as e:
        print("Bad parameter.")
        return "パラメータを正しく設定してください"

    if s_ids == "all":
        s_ids = tles.keys()
    else:
        s_ids = s_ids.split(',')

    print s_ids
    res = {}
    for s_id in [x for x in s_ids if x in tles.keys()]:
        calculator = TLECalculator(tles[s_id])
        r, lat, lng = calculator.calculate_ra_dec(unixtime)[3:6]
        res[s_id] = {
            "time": unixtime,
            "altitude": r - 6378.137,
            "latitude": lat,
            "longitude": lng
        }
    return jsonify(ResultSet=res)


@app.route('/xyz')
def return_txyz():
    """
    開始時刻・終了時刻（・衛星のカタログ ID）を受け取り
    その期間の300秒おきの位置情報（x, y, z）を返す
    """
    # データの時間間隔 [s]
    t_interval = 300
    global tles
    try:
        start_time = request.args.get("start", type=int)
        end_time = request.args.get("end", type=int)
        s_ids = request.args.get("ids", default="all")
    except Exception as e:
        print("Bad parameter.")
        return "パラメータを正しく設定してください"

    if s_ids == "all":
        s_ids = tles.keys()
    else:
        s_ids = s_ids.split(',')

    print s_ids
    res = {}
    for s_id in [x for x in s_ids if x in tles.keys()]:
        calculator = TLECalculator(tles[s_id])
        txyz_list = []
        dt = 0
        while dt <= end_time - start_time:
            x, y, z = calculator.calculate_ra_dec(start_time + dt)[0:3]
            txyz_list.append([dt, x, y, z])
            dt += t_interval
        res[s_id] = txyz_list
    return jsonify(ResultSet=res)


def update_tles():
    """TLE の値を更新する"""
    s = requests.Session()
    # Space-Track にログイン
    s.post(login_url, data=login_data)
    # TLE を取得
    tles_json = s.get(base_url + "basicspacedata/query/class/tle_latest/ORDINAL/1/NORAD_CAT_ID/{0}/orderby/TLE_LINE1 ASC/format/json".format(",".join(satelite_nums))).json()
    res = {}
    for tle in tles_json:
        res[tle["NORAD_CAT_ID"]] = tle
    return res


if __name__ == '__main__':
    # Space-Track から返ってきた TLE (JSON) の辞書（キーはカタログ番号）
    tles = update_tles()
    tle_get_time = time.time()

    # Space-Track からのレスポンスに含まれない番号は除去
    satelite_nums = tles.keys()
    print tle_get_time

    app.run(host='0.0.0.0', debug=True)
