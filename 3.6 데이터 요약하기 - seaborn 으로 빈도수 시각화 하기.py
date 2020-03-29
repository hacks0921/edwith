import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# window 한글폰트 설정
# plt.rc('font',family ='AppleGothic')
plt.rc('font',family ='Malgun Gothic')  # 폰트 설정
plt.rc('axes',unicode_minus=False)

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

a = '의료기관_201909.csv'
df = pd.read_csv(a, low_memory=False)
null_count = df.isnull().sum()  # 결측치 구한 데이터를 null_count 변수에 넣어준다
df_null_count = null_count.reset_index()  # nu_count를 DataFrame 형태로 변환해줄떄 reset_index() 사용
df_null_count.columns = ["컬럼명","결측치수"] # df_null_count의 컬럼명 변경
df_null_count = df_null_count.sort_values(by ="결측치수",ascending=False)  # 결측치수 기준을 가지고 내림차순정열
df_null_count_top  = df_null_count.sort_values(by ="결측치수",ascending=False).head(10) # df_null_count_top에 상위 10개의 컬럼을 넣어줌
drop_columns = df_null_count_top["컬럼명"].tolist()  # 드롭할 컬럼을추출한다 리스트 형태로
df = df.drop(drop_columns,axis = 1)  # df에서 drop_columns 에서 드롭 컬럼을 제거  # 0행, 1열


3.6 데이터 요약하기 - seaborn 으로 빈도수 시각화 하기

print(df["상권업종대분류명"].value_counts())
print(df["상권업종중분류명"].value_counts())
print(df["상권업종중분류명"].value_counts(normalize=True))

c = df["상권업종중분류명"].value_counts()
n = df["상권업종중분류명"].value_counts(normalize=True)

d = df["상권업종소분류명"].value_counts()
m = df["상권업종소분류명"].value_counts(normalize=True)

d.plot.barh(rot=0,figsize =(7,8) , grid = True ) # rotation 0
plt.show()

m.plot.pie()
plt.show()