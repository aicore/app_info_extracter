from utils import Utils
import pandas as pd

class Analytics:
    def __init__(self, name_of_app, package_name, country, lang):
        self.name_of_app = name_of_app
        self.package_name = package_name
        self.lang = lang
        self.country = country

    def __get_file_name(self, score):
        file_name = 'review_' + self.package_name + \
            '_' + self.country + '_'+self.lang+'_'+str(score) + '.csv'
        return file_name

    def __get_count_file_name(self, duration):
        file_name = duration + '_review_count_' + self.package_name + \
            '_' + self.country + '_'+self.lang+'_' + '.csv'
        return file_name

    def __should_count(self, duration):
        file = self.name_of_app + '//' + self.__get_count_file_name(duration)
        return Utils.is_file_present(file)

    def __combine_data(self):
        dir_name = self.name_of_app
        file_name = self.__get_file_name(1)
        path = './/' + dir_name + '//' + file_name
        df = pd.read_csv(path)
        for score in range(2, 6):
            file_name = self.__get_file_name(score)
            path = './/' + dir_name + '//' + file_name
            df1 = pd.read_csv(path)
            df = df.append(df1)
        return df

    def count_reviews_each_month(self):
        if self.__should_count('month'):
            return
        df = self.__combine_data()
        df['at'] = pd.to_datetime(df['at'])
        df.sort_values(by=['at'], ascending=True, inplace=True)
        df1 = df.groupby([df['at'].dt.year, df['at'].dt.month]).agg({'count'})
        no_of_reviews = df1[('at', 'count')].tolist()
        month = df['at'].dt.strftime("%m/%y").drop_duplicates().tolist()
        final_df = pd.DataFrame({'month': month, 'no_of_reviews': no_of_reviews})
        count_file_name = self.__get_count_file_name('month')
        final_df.to_csv(count_file_name, index=None, header=True)
        dir_name = self.name_of_app
        Utils.move_file_to_folder(count_file_name, dir_name)

    def count_reviews_each_week(self):
        if self.__should_count('week'):
            return
        df = self.__combine_data()
        df['at'] = pd.to_datetime(df['at'])
        df.sort_values(by=['at'], ascending=True, inplace=True)
        week = []
        no_of_reviews = []
        week_df = df.groupby(pd.Grouper(key='at', freq='W'))
        for name, group in week_df:
            if len(group) > 0:
                week.append(name)
                no_of_reviews.append(len(group))
        final_df = pd.DataFrame({'week': week, 'no_of_reviews': no_of_reviews})
        count_file_name = self.__get_count_file_name('week')
        final_df.to_csv(count_file_name, index=None, header=True)
        dir_name = self.name_of_app
        Utils.move_file_to_folder(count_file_name, dir_name)