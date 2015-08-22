#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sergey Tsaplin'
SITENAME = u'sergeytsaplin.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Nicosia'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (#('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/notmyidea'

STATIC_PATHS = ['images', 'extras/CNAME']
EXTRA_PATH_METADATA = {
	'extras/CNAME': {'path': 'CNAME'},
}

SINGLE_AUTHOR = True

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

ARTICLE_LANG_URL = '{lang}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}/index.html'

GITHUB_URL = 'https://github.com/SergeyTsaplin'
TWITTER_USERNAME = 'SergeyTsaplin'

SOCIAL = (
	('twitter', 'https://twitter.com/SergeyTsaplin'),
	('facebook', 'https://www.facebook.com/sergeytsaplin'),
	('vk', 'https://vk.com/sergey_tsaplin'),
)
