import pandas as pd
from tqdm import tqdm
from google_play_scraper import app, reviews_all, Sort
from utils import Utils
import time
from tabulate import tabulate


class Scrapper:
    def __init__(self, name_of_app, package_name, country, lang):
        if not package_name or not lang or not country or not name_of_app:
            raise ValueError("Invalid parameters passed for scrapping")
        self.name_of_app = name_of_app
        self.package_name = package_name
        self.lang = lang
        self.country = country
        app_info = app(self.package_name, self.lang, self.country)
        del app_info["comments"]
        Utils.print_json(app_info)
        self.app_info = app_info
        self.reviews = {}

    def scrap_review(self):
        """This method will scrap the google play store for getting reviews of
        the given app. This method will iteratively read reviews from rating
        1 to 5. This method will be executed only once the result of this
        method will be cached to prevent expensive network calls"""
        if self.reviews:
            return self.reviews

        for score in tqdm(range(1, 6)):
            print()
            print('scarpping for score ' + str(score))
            self.__scrap_reviews(score)
            self.__print_and_save(score)
            print('waiting for 1 minute ')
            time.sleep(60)

    def __print_and_save(self, score):
        self.__print_summary()
        self.__save_results(score)

    def __print_summary(self):
        self.scrap_review()
        print('Score \t number of entries')
        results_to_print = []

        for score in self.reviews:
            results_to_print.append([score, len(self.reviews[score])])
        table = tabulate(results_to_print, ['Score', 'Number Of Entries'])
        print(table)

    def __scrap_reviews(self, score):
        result = reviews_all(
            self.package_name,
            sleep_milliseconds=0,  # defaults to 0
            lang=self.lang,  # defaults to 'en'
            country=self.country,  # defaults to 'us'
            sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
            filter_score_with=score,  # defaults to None(means all score)
        )
        self.reviews[score] = result

    def __save_results(self, score):
        dir_name = self.name_of_app
        Utils.create_directory_if_not_exit(dir_name)
        print("Results directory  " + dir_name)
        app_reviews_df = pd.DataFrame(self.reviews[score])
        file_name = 'review_' + self.package_name + \
            '_' + self.country + '_' + str(score) + '.csv'
        app_reviews_df.to_csv(file_name, index=None, header=True)
        # Hack as  pandas create file only in current folder
        # TODO: Fix this cleanly
        Utils.move_file_to_folder(file_name, dir_name)


class Crawler:
    def __init__(self, config_file):
        self.config = Utils.read_yaml_config_file(config_file)

    def crawl(self):
        jobs = self.__prepare_crawler()
        for job in tqdm(jobs):
            job.scrap_review()
            # job.print_summary()
            # job.save_results()

    def __prepare_crawler(self):
        jobs = []
        for package in self.config['Apps']:
            jobs.extend(
                self.__prepare_package_for_crawling(
                    package, self.config['Apps'][package]))
        return jobs

    def __prepare_package_for_crawling(self, package, package_info):
        jobs = []
        package_name = package_info['package_name']
        for country_lang in package_info['geographies_languages']:
            split = country_lang.split(',')
            country = split[0].strip()
            lang = split[1].strip()
            scrapper = Scrapper(package, package_name, country, lang)
            jobs.append(scrapper)
        return jobs
