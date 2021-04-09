## Introduction
App info extractor is a utility to extract and analyze customer reviews and critical metrics of apps from multiple sources like google play store, Apple play store, and any other sources.This utility is highly configurable to extract and give relevant information about any app in a meaningful way.

## How it works?
This utility takes config.yaml as input. Configuration for each app is self-contained in configs. Once a configuration is specified in config.yaml, the utility will iteratively go through each app, crawl the relevant information, and store the data locally as a CSV file.

## How to use it?
1. Check out the package
2. Have python 3.8 on your system . Use [pyenv](https://github.com/pyenv/pyenv) to manage multiple version of python in your machine
3. Open terminal and type  ``` cd app_info_extracter```
4. Setup python [virtual enviorment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) having this will prevent you from messing up with the system-wide python installation
5. Now type in terminal ``` cd src/crawler/```
6. Add the required configuration in config.yaml using your favorite editor
7. in terminal type ```python main.py config.yaml```
8. Results of the crawling will be stored in  separate directories for  each app in current directory 
9. In case of failure, just re-run ```python main.py config.yaml```  script will start from where its left off.

## Contributing
1.Use vim or InteliJUltimate or pycharm or visualstudio code.


