import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

GOOGLE_API_KEY = env('GOOGLE_API_KEY')

BOT_NAME = "scrapy_parser"

SPIDER_MODULES = ["scrapy_parser.spiders"]
NEWSPIDER_MODULE = "scrapy_parser.spiders"

ROBOTSTXT_OBEY = True


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
