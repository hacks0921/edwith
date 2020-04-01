import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
if os.name == 'posix':
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")
plt.rc("axes", unicode_minus=False)
# % configInlineBackend.figure_format = 'retina'

csv_name = "건강검진정보(2017).csv"
df = pd.read_csv(csv_name, encoding ="cp949") # 한글변환 CP949
# print(df.shape)
# print(df)
# print(df.head(10))
# print("-----------------------")
# print(df.info)
# print("-----------------------")
# print(df.columns)
# print("-----------------------")
# print(df.dtypes)
# print("-----------------------")
# print(df.isnull)
# print(df.isnull().sum())
# df.isnull().sum().plot.barh(figsize=(10,9))
# a = df.isnull().sum()   #bar 세로, barh 가로
# a.plot.barh(figsize=(10,9))
# plt.show()
# print(df["(혈청지오티)AST"]) # 씨리즈 형태
# print(df[["(혈청지오티)ALT","(혈청지오티)AST"]])  # DF형태
# print(df["(혈청지오티)AST"].head())
# print(df[["(혈청지오티)ALT","(혈청지오티)AST"]].describe())
# print(df["성별코드"].value_counts())  # 성별 코드의 종류와 개수를 볼 수 있다
# print(df["흡연상태"].value_counts())

a = df.groupby(["성별코드"]).mean()
b = df.groupby(["성별코드"]).count()
c = df.groupby(["성별코드","음주여부"])["가입자일련번호"].count()
d= df.groupby(["성별코드","음주여부"])["감마지피티"].mean()
e = df.groupby(["성별코드","음주여부"])["감마지피티"].describe()
f = df.groupby(["성별코드", "음주여부"])["감마지티피"].agg(["count", "mean", "median"])
# 성별코드, 음주여부에 따라 가입자 일련번호의 개수

e = df.pivot_table(index = "음주여부", values = "가입자일련번호", aggfunc ="count")
 # DF 변환 . 직관적 사용 가능, 속도는 조금더 느리다
f = df.pivot_table(index = "음주여부", values = "가입자일련번호", aggfunc="count")
g = df.pivot_table(index = "음주여부", values = "감마지피티")
h = df.pivot_table(index = "음주여부", values = "감마지피티", aggfunc="mean","median")
i = df.pivot_table(index = "음주여부", values = "감마지피티", aggfunc="describe")
j = df.pivot_table(index = ["음주여부","성별코드"], values = "감마지피티", aggfunc="describe")
print(j)

print("완료")

