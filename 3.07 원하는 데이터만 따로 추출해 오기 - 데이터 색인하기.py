import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family ='Malgun Gothic')  # 폰트 설정
plt.rc('axes',unicode_minus=False)
from IPython.display import set_matplotlib_formats
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

# 3.7 원하는 데이터만 따로 추출해 오기 - 데이터 색인하기 데이터 색인하기

# 1차) 대분류 구분후에 중분류 개수 확인
print(df[df["상권업종대분류명"] == "의료"])
print(df.loc[df["상권업종대분류명"] == "의료","상권업종중분류명"])
print(df.loc[df["상권업종대분류명"] == "의료","상권업종중분류명"].value_counts())

# 2차)변수에 담아서 대분류 구분후에 중분류 개수 확인
m = df["상권업종대분류명"] == "의료"
print(df.loc[m,"상권업종중분류명"].value_counts())
print(df[df["상권업종중분류명"]=="유사의료업"].shape)
print(df["상호명"].value_counts().head(10))  #method chain 방법 사용

# 2개 이상의 중목 조건을 사용할 경우
df_seoul_drug = df[(df["상권업종소분류명"]=="약국")  &  (df["시도명"]=="서울특별시")]
# and 조건을 수행할떄 () & ()으로 해줘야 함
# or조건을 수행할떄 () | ()으로 해줘야 함
print(df_seoul_drug)
print(df_seoul_drug.shape)
print(df_seoul_drug.head(5))




