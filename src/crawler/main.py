from scraper import Crawler
import argparse

# scraper = Crawler('config.yaml')
# scraper.crawl()

parser =argparse.ArgumentParser(prog='App Info Extracter', usage='''python main.py <file> ''',
description='''Description:
App info extractor is a utility to extract and analyze customer reviews and critical metrics of apps from multiple
sources like google play store, Apple play store, and anyother sources.This utility is highly configurable to extract
and give relevant information about any app in a meaningful way.''',
formatter_class=argparse.RawDescriptionHelpFormatter,
add_help=True
)
parser.add_argument("file", type=str,
help="config.yaml file containing the configuration for each app"
)
arg = parser.parse_args()
scraper = Crawler(arg.file)
scraper.crawl()