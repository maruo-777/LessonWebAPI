# coding: UTF-8
import requests
from bs4 import BeautifulSoup

TARGET_URL = "https://news.yahoo.co.jp/pickup/6412775" # スクレイピングしたいURLをここに書く

html = requests.get(TARGET_URL)  # HTMLを取ってくる
soup = BeautifulSoup(html.content, "html.parser")  # HTMLを解析する
title = soup.find("title")  # データを抽出する
print(title)