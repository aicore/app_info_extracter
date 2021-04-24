## Introduction
App info extractor is a utility to extract and analyze customer reviews and critical metrics of apps from multiple sources like google play store, Apple play store, and any other sources.This utility is highly configurable to extract and give relevant information about any app in a meaningful way.

## How it works?
This utility takes config.yaml as input. Configuration for each app is self-contained in configs. Once a configuration is specified in config.yaml, the utility will iteratively go through each app, crawl the relevant information, and store the data locally as a CSV file.

## How to use it?
1. Check out the package
2. Have python 3.8 on your system . Use [pyenv](https://github.com/pyenv/pyenv) to manage multiple version of python in your machine
3. Open terminal and type  ``` cd app_info_extracter```
4. Setup python [virtual enviorment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) having this will prevent you from messing up with the system-wide python installation
5. Run ```pyb install_dependencies``` to install the dependencies for your project. Refer to the **Building and testing** section below incase of queries.
6. To check if the build is successful, run ```pyb``` in the terminal.
7. Add the required configuration in config.yaml using your favorite editor
8. In terminal type ```python3 src/crawler/main.py src/crawler/config.yaml```
9. Results of the crawling will be stored in  separate directories for  each app in current directory 
10. In case of failure, just re-run ```python3 src/crawler/main.py src/crawler/config.yaml```  script will start from where its left off.

## Building and testing
### Prerequisites
1. Verify that Python-3 and pip3 should be installed in your system. terminal>`pip3 -V`
2. Install pyb:  `pip3 install pybuilder`
3. Verify Pyb  installation :`pyb --version`

### To build,clean and run tests, use the following command:
#### Build and test
```shell
pyb install_dependencies 
# Pyb should work without pyb install_dependencies, but unfortunately it doesnt.
# See details: here https://github.com/pybuilder/pybuilder/issues/727 
pyb -v
```
* That's all you need to build the project.
* Details about Test failures if any can be found in file `target\reports\unittest`
* The binary artifacts will be available in the target folder.
#### Clean builds :
* > pyb clean
  
#### Reset environment :
* > pyb clean && rm -rf .pybuilder

### working with the build system
* Tutorial: https://pybuilder.io/documentation/tutorial
* To make changes to build scripts see this: https://pythonhosted.org/pybuilder/walkthrough-new.html

## IDE setup
* [Pycharm/intellij](https://www.jetbrains.com/pycharm/) support is present in source. `.idea` files are avilable when you clone this repo. Just open the folder in pycharm.

## Contributing
* Use vim or InteliJUltimate or pycharm or visualstudio code.


