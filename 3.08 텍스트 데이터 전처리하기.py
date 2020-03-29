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
df_seoul_drug = df[(df["상권업종소분류명"]=="약국")  &  (df["시도명"]=="서울특별시")]  # and 조건을 수행할떄 () & ()으로 해줘야 함

c =  df_seoul_drug["시군구명"].value_counts()
print(c.head())

n =  df_seoul_drug["시군구명"].value_counts(normalize = True)
print(n.head())


# c.plot.bar(rot=60)
# plt.show()

print(df[df["상권업종소분류명"]=="종합병원"])
print(df[   (df["상권업종소분류명"]=="종합병원")
           &(df["시도명"]=="서울특별시")])

df_seoul_hospital = df[(df["상권업종소분류명"]=="종합병원")&(df["시도명"]=="서울특별시")].copy()
print(df_seoul_hospital["시군구명"].value_counts())

a = ~df_seoul_hospital["상호명"].str.contains("종합병원")  # 종합병원이 아닌것만 ~ 표시 하면 됨
print(a)

print(df_seoul_hospital.loc[~df_seoul_hospital["상호명"].str.contains("종합병원"),"상호명"].unique())

df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("꽃배달")]
df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기")]

b = df_seoul_hospital["상호명"].str.contains("꽃배달|의료기|장례식장|상담소|어린이집")
print(b)

c = df_seoul_hospital["상호명"].str.contains("꽃배달|의료기|장례식장|상담소|어린이집").index
print(c)

drop_row = df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("꽃배달|의료기|장례식장|상담소|어린이집")].index
print(drop_row)
drop_row = drop_row.tolist()
print(drop_row)


drop_row2 =  df_seoul_hospital[df_seoul_hospital["상호명"].str.endswith("의원")].index
drop_row2 = drop_row2.tolist()
print(drop_row2)

drop_row = drop_row + drop_row2
print(drop_row)
print(len(drop_row))
print("---------------------------------------")
print(df_seoul_hospital.shape)
df_seoul_hospital = df_seoul_hospital.drop(drop_row,axis = 0 )  # 행을 기준으로 삭제 함
print(df_seoul_hospital.shape)

print("---------------------------------------")

d = df_seoul_hospital["시군구명"].value_counts()
print(d)

plt.figure(figsize= (15,4))
sns.countplot(data = df_seoul_hospital, x="시군구명",
              order=df_seoul_hospital["시군구명"].value_counts().index)  # 값이 높은 순서대로 정렬
plt.show()

e = df_seoul_hospital["상호명"].unique()
print(e)
