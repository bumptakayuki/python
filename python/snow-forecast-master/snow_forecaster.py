# -*- coding: utf-8 -*-

import csv
from sklearn.svm import LinearSVC
from sklearn.ensemble import AdaBoostClassifier,ExtraTreesClassifier,GradientBoostingClassifier,RandomForestClassifier
from sklearn.decomposition import TruncatedSVD
from sklearn import datasets
from sklearn.cross_validation import cross_val_score
import sys
import cgi
import os

class SnowForecast:

    CLF_NAMES = ["LinearSVC","AdaBoostClassifier","ExtraTreesClassifier" ,
                 "GradientBoostingClassifier","RandomForestClassifier"]

    def __init__(self):
        u"""各インスタンス変数を初期化"""
        self.clf = None
        self.data = {"target" : [], "data" : []}
        self.weather_data = None
        self.days_data = {}
        self.days_snow = {}

    #学習用CSVファイルを読み込む
    def load_csv(self): 
        path = os.path.abspath(os.path.dirname(__file__))
        fileName = "sample_data/data.csv"
        with open(path +'/'+ fileName, "r") as f:
            reader = csv.reader(f)
            accumulation_yesterday = 0
            temp_yeaterday = 0
            date_yesterday = ""
            
            #csvデータの数だけ繰り返す
            for row in reader:

                # 空の場合、読み飛ばす
                if row[4] == "":
                   continue

                daytime = row[0] #時間
                date = daytime.split(" ")[0] #日時
                temp = int(float(row[1])) #
                accumulation = int(row[4])
                wind_speed = float(row[7])
                precipitation = float(row[12])

                if date_yesterday != "":
                    # 1行分 [温度, 降水量, 昨日の温度, 昨日の積雪量]
                    sample = [temp, precipitation, temp_yeaterday, accumulation_yesterday]
                    #積もったかの判定情報を返却する
                    exist = self.accumulation_exist(accumulation)

                    #データ解析用の変数に格納する
                    self.data["data"].append(sample)
                    self.data["target"].append(exist)
                    #一日単位の積雪状態
                    self.days_data[daytime] = sample
                    #積雪したか
                    self.days_snow[daytime] = exist

                if date_yesterday != date:
                    accumulation_yesterday = accumulation
                    temp_yeaterday = temp
                    date_yesterday = date

        return self.data

    #0 積雪量(cm)を受け取り、積雪があれば１、なければ0を返す
    def accumulation_exist(self, accumulation):
        if accumulation > 0:
            return 1
        else:
            return 0

    #1 学習を実行する。実際の学習の前にどのモデルを使うかを判定し、自動的に選択させる。
    def train(self):
        self.clf = self.best_score_clf()
        self.clf.fit(self._features(), self._labels())

    #2 各学習モデルのタイプ別にスコアを計算し、もっともスコアの高いタイプのオブジェクトをインスタンス変数にとっておく.
    def best_score_clf(self):
        features = self._features()
        labels = self._labels()

        # 今回は特徴量の算出に4量しか使わないので特徴量の削減は行わない。よって以下はコメントにしておく。
        # lsa = TruncatedSVD(3)
        # reduced_features = lsa.fit_transform(features)

        best = LinearSVC()
        best_name = self.CLF_NAMES[0]
        best_score = 0

        for clf_name in self.CLF_NAMES:
            clf    = eval("%s()" % clf_name) 
            scores = cross_val_score(clf, features, labels, cv=5) # 特徴量削減した場合は reduced_features を使う
            score  = sum(scores) / len(scores)  #モデルの正解率を計測
            # print("%sのスコア:%s" % (clf_name,score))
            print(  (score))

            if score >= best_score:
                best = clf
                best_name = clf_name
                best_score = score

        print("------\n %s" % best_name)
        return clf

    #3 学習データを返す。
    def _features(self):
        weather = self.train_data()
        return weather["data"]

    #4 結果のラベルを返す。
    def _labels(self):
        weather = self.train_data()
        return weather["target"]

    #5 学習を行うためのデータを返す。すでに読み込み済みならそれを返し、まだならCVSファイルから読み込む
    def train_data(self):
        if self.weather_data is None:
            self.weather_data = self.load_csv()

        return self.weather_data


    #####################################################
    # その他の検証用メソッド
    #####################################################

    #雪が積もったなら1、積もらなければ0を返す
    def is_snow_exist(self, daytime_str):
        return self.days_snow[daytime_str]

    #与えられた日付のデータを使って積雪の有無を予想する。
    def predict_with_date(self, daytime_str):
        sample = self.days_data[daytime_str]
        temp = sample[0]
        precipitation = sample[1]
        temp_yeaterday = sample[2]
        accumulation_yesterday = sample[3]
        return self.predict(temp, precipitation, temp_yeaterday, accumulation_yesterday)
    
    #与えられたパラメータを使って積雪の有無を予想する。
    def predict(self, temp, precipitation, temp_yeaterday, accumulation_yesterday):
        return self.clf.predict([[temp, precipitation, temp_yeaterday, accumulation_yesterday]])[0]

    #日付文字列を受け取って積雪判定を行う。
    def judge(self, datetime_str):
        print("------")
        result = forecaster.predict_with_date(datetime_str)
        print("%s: 予想:%s 実際:%s" % (datetime_str, result, forecaster.is_snow_exist(datetime_str)))

        if result == 1:
            print("雪が積もります")
        else:
            print("雪は積もらないです")


#######################################
# メインの処理 パラメータを直接与えて予測させてみる。
#######################################
if __name__ == "__main__":

    #機械学習実行
    forecaster = SnowForecast()
    forecaster.train()

    print("------")

    param = sys.argv

    temp = param[1]
    precipitation = param[2]
    temp_yeaterday = param[3]
    accumulation_yesterday = param[4] 

    result = forecaster.predict(temp, precipitation, temp_yeaterday, accumulation_yesterday)
    
    print("[温度:%s] [降水量:%s] [昨日の温度:%s] [昨日の積雪量:%s]" %
          (temp, precipitation, temp_yeaterday, accumulation_yesterday))

    print("判定結果: %s" % result)
    
    if result == 1:
        print("雪が積もります")
    else:
        print("雪は積もらないです")
