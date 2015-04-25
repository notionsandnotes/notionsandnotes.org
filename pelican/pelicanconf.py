#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

DELETE_OUTPUT_DIRECTORY = True

AUTHOR = u'George S.'
SITENAME = u'Notions and Notes'
SITESUBTITLE = u'Notes on mathematical notions'
SITEURL = 'http://www.notionsandnotes.org'

EMAIL_ADDR = 'notionsandnotes at notionsandnotes dot org'

DEFAULT_LANG = u'en'
TIMEZONE = 'Europe/Berlin'

DEFAULT_DATE_FORMAT = '%d %B %Y'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['code_include','extract_toc','render_math','better_figures_and_images','series','related_posts','summary','better_codeblock_line_numbering']

from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension
MD_EXTENSIONS = [
    CodeHiliteExtension(css_class='highlight', linenums=False),
    TocExtension(),
    'markdown.extensions.extra',
]

TYPOGRIFY = True

USE_OPEN_GRAPH = False


PATH = '../raw'
OUTPUT_PATH = '../www.notionsandnotes.org/'


STATIC_PATHS = ['extra', 'images', 'pdfs']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'},
    'extra/custom.css': {'path': 'custom.css'},
}

PLUGINS += ['subcategory']
CATEGORIES_SAVE_AS = 'categories.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
SUBCATEGORY_SAVE_AS = 'category/{savepath}/index.html'
SUBCATEGORY_URL = 'category/{savepath}/'
ARTICLE_URL = '{suburl}/{slug}.html'
ARTICLE_SAVE_AS = '{subpath}/{slug}.html'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
SUBCATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

TAGS_SAVE_AS = 'tag.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

THEME = 'themes/pelican-bootstrap3'

sys.path.append(os.curdir)
from themeconf import *

##########################

TAG_CLOUD_STEPS = 4

##########################
#######################
#######################


# Blogroll
LINKS = (('Bookmarks','http://www.notionsandnotes.org/pages/math-links.html'),
         ('ArXiv', 'http://arxiv.org/archive/math/'),
         ('Mathscinet', 'http://www.ams.org/mathscinet/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/notionsandnotes'),
          ('Stack Exchange', 'http://math.stackexchange.com/users/230418/'),
	  ('Twitter', 'https://twitter.com/NotionsandNotes'),
          ('Facebook','https://www.facebook.com/notionsandnotes'),
          )


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

RELATIVE_URLS = True

