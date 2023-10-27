""" Settings added as specified in following link
http://docs.gunicorn.org/en/stable/settings.html
"""

from the_onahs import config as conf

accesslog = '-'

bind = '{}:{}'.format(conf.HOST, conf.PORT)
workers = 6
threads = 2
