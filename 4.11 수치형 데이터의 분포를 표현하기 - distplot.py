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
df_sample = df.sample(1000,random_state=1)
print(df.columns)

★★★★★★★★★수치형 데이터★★★★★★★★★★

■■■■■ hist : 빈도수 그림(히스토그램)

# df["총콜레스테롤"].notnull() # 마스크로 생성됨 df로 감싸줘야 함
# loc를 이요하여 총콜레스테롤만 시리즈 형태로 가지고온다
df_chol = df.loc[df["총콜레스테롤"].notnull(), "총콜레스테롤"]   #데이터가 없능 항목은 제외하고 그리기
print(df_chol.dtypes)
 # 시리즈 형태로 가지과야하기떄문에 loc를 사용함
sns.distplot(df_chol, bins=10)
sns.distplot(df_chol)

df[df["총콜레스테롤"].notnull() & (df["음주여부"] == 1)]
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"])
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"])
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"], hist=False)
#히스트그램을 안그리고 선만 그릴떄 hist = false
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"])

# kdeplot 부드러운 곡선으로 그릴떄
sns.kdeplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"])
sns.kdeplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"])

plt.axvline(df_sample["총콜레스테롤"].mean(), linestyle=":") # 평균, 중앙값을 넣어줌
plt.axvline(df_sample["총콜레스테롤"].median(), linestyle="--")
sns.kdeplot(df_sample.loc[(df_sample["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"], label="음주 중")
sns.kdeplot(df_sample.loc[(df_sample["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"], label="음주 안 함")

print(df_sample["음주여부"] == 1)
print(df_sample[df_sample["음주여부"] == 1])
print(df_sample.loc[df_sample["음주여부"] == 1, "감마지티피"])

■■■■■ his 그래프 그리기■■■■■
s_1 = df_sample.loc[(df_sample["음주여부"] == 1) & (df_sample["음주여부"].notnull()), "감마지티피"]
s_0 = df_sample.loc[(df_sample["음주여부"] == 0) & (df_sample["음주여부"].notnull()), "감마지티피"]
sns.distplot(s_1,bins=100)
sns.distplot(s_0,bins=100)

#distplot 사용시 시리즈 형태로 ㄴ허어줘야 한다, 행, 열 형태로
plt.show()