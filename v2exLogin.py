#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cookielib
import urllib
import urllib2
from pyquery import PyQuery

#需要pyquery，ubuntu下可直接执行sudo apt-get install python-pyquery进行安装

USER = 'your_user_name'
PASSWORD = 'your_password'
BASE_URL = "http://www.v2ex.com"

SIGNIN_URL = BASE_URL + '/signin'
MISSION_URL = BASE_URL + '/mission/daily'

header = {
    'Referer': SIGNIN_URL
    }

cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
signin_req = urllib2.Request(SIGNIN_URL)
signin_resp = urlOpener.open(signin_req)


signin_query = PyQuery(signin_resp.read())
# 获取once input 的值
onceInput = signin_query('input[name="once"]')
onceVal = onceInput.val()


values = {'u': USER, 'p': PASSWORD, 'once': onceVal}
data = urllib.urlencode(values)

# 进行登录
login_req = urllib2.Request(SIGNIN_URL, data, header)
login_resp = urlOpener.open(login_req)

if not 'auth' in [cookie.name for cookie in cookiejar]:
	raise ValueError, "登录失败!"

# 请求任务页面
mission_req = urllib2.Request(MISSION_URL)
mission_page = urlOpener.open(mission_req).read()

if ("每日登录奖励已领取" in mission_page):
    print "每日登录奖励已领取"
    exit(0)

# 获取领取按钮的链接并请求
mission_query = PyQuery(mission_page)
href = mission_query("input.super").attr("onclick")

get_coin_href = href[href.index("'")+1:len(href)-2]
get_coin_req = urllib2.Request(BASE_URL + get_coin_href)
get_coin_page = urlOpener.open(get_coin_req).read()

if ("已成功领取每日登录奖励" in get_coin_page):
    print "已成功领取每日登录奖励"
