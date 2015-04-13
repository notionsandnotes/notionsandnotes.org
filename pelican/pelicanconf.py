#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DELETE_OUTPUT_DIRECTORY = True

AUTHOR = u'George S.'
SITENAME = u'Notions and Notes'
SITEURL = 'http://www.notionsandnotes.org'

EMAIL_ADDR = 'notionsandnotes at notionsandnotes dot org'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['code_include','extract_toc','render_math','better_figures_and_images','assets','series','related_posts','subcategory','summary']

from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension
MD_EXTENSIONS = [
    CodeHiliteExtension(css_class='highlight'),
    TocExtension(permalink=True),
    'markdown.extensions.extra',
]

TYPOGRIFY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = u'en'
TIMEZONE = 'Europe/Berlin'

DEFAULT_DATE_FORMAT = '%d %B %Y'
DEFAULT_CATEGORY = "General"

PATH = '../raw'
OUTPUT_PATH = '../www.notionsandnotes.org/'
STATIC_PATHS = ['extra', 'images', 'pdfs']


EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'}
}

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'

#PLUGINS = PLUGINS + ['custom_article_urls']

#CUSTOM_ARTICLE_URLS = {
#    'Analysis': {'URL': '{category}/{slug}/',
#                 'SAVE_AS': '{category}/{slug}/index.html'},
#    }

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

THEME = 'themes/built-texts'

COLOPHON = True
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = "Mainly notes, activity log, and sometimes personal blog, of an amateur mathematician, by which it is meant that the author did go through graduate school, but did not complete it to a Ph. D.. Obviously he still maintains interest in the same. Resuming mathematics full-time seems hard against the severe demands of life. The years rush by, but the dream persists. Borrowing Robert Browning,<br><br><center><a href='http://www.bartleby.com/42/675.html'>Ah, but a man's reach should exceed his grasp,<br>Or what's a heaven for?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></center><br><br>Contact can made be via Twitter or e-mail to notionsandnotes at notionsandnotes dot org."

##########################
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

