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

print(a)
print(df.shape)
print(df.head)
print(df.head(1))
# print(df.head(tail(1)))
print(df.tail(1))
print(df.info())
# print(df.dtpye)
print("-------------------------")
print(df.isnull())  # 결측치를 확인하고
print("-------------------------")
print(df.isnull().sum())  # 결측치를 합쳐서 보여준다 컬럼에 대해서
print("-------------------------")
null_count = df.isnull().sum()  # 결측치 구한 데이터를 null_count 변수에 넣어준다
print(null_count)
print("-------------------------")
# null_count.plot()
# null_count.plot.bar(rot=60)  #bar chart
# null_count.plot.barh(figsize = (5,7))  # hbar 형태로 null_count를 그래프로 그려준다
df_null_count = null_count.reset_index()  # nu_count를 DataFrame 형태로 변환해줄떄 reset_index() 사용
print(df_null_count)
print("-------------------------")

print(df_null_count.head()) # df_null_count의 상쉬 항목 보여주기
print(df_null_count.columns)  #df_null_count의 컬럼 이름을 보여줌
df_null_count.columns = ["컬럼명","결측치수"] # df_null_count의 컬럼명 변경
print(df_null_count.columns)  # df_null_count columns 컬럼 이름 보여주기
print("-------------------------")
print(df_null_count)
# df_null_count= df_null_count.sort_values(by ="결측치수")
df_null_count = df_null_count.sort_values(by ="결측치수",ascending=False)  # 결측치수 기준을 가지고 내림차순정열
print("-------------------------")
print(df_null_count)
# plt.show()
print("-------------------------")
print(df["지점명"])
df_null_count_top  = df_null_count.sort_values(by ="결측치수",ascending=False).head(10) # df_null_count_top에 상위 10개의 컬럼을 넣어줌
print(df_null_count_top)
print(df_null_count_top["컬럼명"]) # 컬럼 이름만 보여줌
drop_columns = df_null_count_top["컬럼명"].tolist()  # 드롭할 컬럼을추출한다 리스트 형태로
print(drop_columns)
print("-------------------------")
print(df[drop_columns])  # drop_columns을 df형태로 변환해준다
print("-------------------------")
print(df[drop_columns].head())  # drop_columns을 df형태로 변환해준다
print(df.shape)
'''
df = df.drop(drop_columns,axis = 1)  # df에서 drop_columns 에서 드롭 컬럼을 제거  # 0행, 1열
print(df.shape) # df 형태
print(df.info())  # df 정보 _dataframe 형태로 나옴
print(df.info) # df 정보
print("완료")
'''
