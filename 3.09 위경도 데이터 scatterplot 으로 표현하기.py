import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family ='Malgun Gothic')  # 폰트 설정
plt.rc('axes',unicode_minus=False)
from IPython.display import set_matplotlib_formats
import seaborn as sns
set_matplotlib_formats('retina')

a = '의료기관_201909.csv'
df = pd.read_csv(a, low_memory=False)
print("-----------------------------------------")
print(df)
null_count = df.isnull().sum()  # 결측치 구한 데이터를 null_count 변수에 넣어준다
df_null_count = null_count.reset_index()  # nu_count를 DataFrame 형태로 변환해줄떄 reset_index() 사용
df_null_count.columns = ["컬럼명","결측치수"] # df_null_count의 컬럼명 변경
df_null_count = df_null_count.sort_values(by ="결측치수",ascending=False)  # 결측치수 기준을 가지고 내림차순정열
df_null_count_top  = df_null_count.sort_values(by ="결측치수",ascending=False).head(10) # df_null_count_top에 상위 10개의 컬럼을 넣어줌
drop_columns = df_null_count_top["컬럼명"].tolist()  # 드롭할 컬럼을추출한다 리스트 형태로
df = df.drop(drop_columns,axis = 1)  # df에서 drop_columns 에서 드롭 컬럼을 제거  # 0행, 1열

df_seoul_drug = df[(df["상권업종소분류명"]=="약국")  &  (df["시도명"]=="서울특별시")]  # and 조건을 수행할떄 () & ()으로 해줘야 함
c =  df_seoul_drug["시군구명"].value_counts()
n =  df_seoul_drug["시군구명"].value_counts(normalize = True)
df_seoul_hospital = df[(df["상권업종소분류명"]=="종합병원")&(df["시도명"]=="서울특별시")].copy()
a = ~df_seoul_hospital["상호명"].str.contains("종합병원")  # 종합병원이 아닌것만 ~ 표시 하면 됨
df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("꽃배달")]
df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기")]
b = df_seoul_hospital["상호명"].str.contains("꽃배달|의료기|장례식장|상담소|어린이집")
c = df_seoul_hospital["상호명"].str.contains("꽃배달|의료기|장례식장|상담소|어린이집").index
drop_row = df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("꽃배달|의료기|장례식장|상담소|어린이집")].index
drop_row = drop_row.tolist()
drop_row2 =  df_seoul_hospital[df_seoul_hospital["상호명"].str.endswith("의원")].index
drop_row2 = drop_row2.tolist()
drop_row = drop_row + drop_row2
df_seoul_hospital = df_seoul_hospital.drop(drop_row,axis = 0 )  # 행을 기준으로 삭제 함
d = df_seoul_hospital["시군구명"].value_counts()
# plt.figure(figsize= (15,4))
# sns.countplot(data = df_seoul_hospital, x="시군구명",
#               order=df_seoul_hospital["시군구명"].value_counts().index)  # 값이 높은 순서대로 정렬

print('============================================')
df_seoul= df[df["시도명"]=="서울특별시"].copy()  # 시도명이 서울특별시인 데이터만 추출


# ■■■막대그래프 그리기
# plot 사용
a = df_seoul["시군구명"].value_counts()
a.plot.bar(figsize =(10,4), rot=30)
# Seaborn 사용
plt.figure(figsize = (15,4))
sns.countplot(data = df_seoul, x = "시군구명")

# ■■■Scatter Plot 그리기
# plot.scatter 사용
b = df_seoul[["경도","위도","시군구명"]]
b.plot.scatter(x="경도" ,y="위도",figsize=(8,7), grid = True)
# seaborn.scatterplot 사용
plt.figure(figsize=(10,10))
sns.scatterplot(data = b, x="경도",y="위도", hue = "시군구명")
plt.show()

