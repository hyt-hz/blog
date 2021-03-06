#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Huang Yiting'
SITENAME = u"HYT's blog"
SITEURL = u'http://blog.yitinghuang.com'

GITHUB_URL = 'https://github.com/hyt-hz/blog'

DISQUS_SITENAME = u'hytblog'

GOOGLE_ANALYTICS = u'UA-44782525-1'
DOMAIN_NAME = u'yitinghuang.com'

TIMEZONE = 'Asia/BeiJing'

DEFAULT_LANG = u'zh'

THEME = 'theme/pelican-bootstrap3'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/hyt-hz/'),
          ('linkedin', 'http://cn.linkedin.com/pub/yiting-huang/26/97b/bb7'),
          ('weibo', 'http://weibo.com/u/2008984445'),
          ('google-plus', 'https://plus.google.com/117508306953808941543'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
