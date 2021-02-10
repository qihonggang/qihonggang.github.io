# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    # "name": "Galileo",
    # "type": "local",
    # "path": "../Galileo"

    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "qihonggang/qihonggang.github.io@gh-pages"
}

# 站点设置
site_name = "我的个人博客"
site_logo = "${static_prefix}mylogo.png"
site_build_date = "2021-2-10T19:49+08:00"
author = "Hogan"
email = "sxxzqhg@gmail.com"
author_homepage = ""
description = "JUST DO IT ! ! !"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Github",
        "url": "https://github.com/qihonggang",
        "brief": "Github"
    },
    {
        "name": "Twitter",
        "url": "https://twitter.com/qihonggang",
        "brief": "twitter"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/qihonggang",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/qihonggang",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/u/3896420238",
        "icon": "gi gi-weibo"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "5yiD3qya7F59X8bkN8tyr9vY-9Nh9j0Va",
    "appKey": "aQrMs1hTwcB1ftqiR4ifJBbh",
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
