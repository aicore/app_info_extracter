# (C) Copyright 2021 core.ai (https://core.ai/) 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Contributors: Dhruv Eldho Peter and others[see commit log]

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