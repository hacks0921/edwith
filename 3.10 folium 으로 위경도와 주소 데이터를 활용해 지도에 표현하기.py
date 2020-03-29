import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family ='Malgun Gothic')  # 폰트 설정
plt.rc('axes',unicode_minus=False)
from IPython.display import set_matplotlib_formats
import folium

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

print('============================================')
df_seoul= df[df["시도명"]=="서울특별시"].copy()  # 시도명이 서울특별시인 데이터만 추출
df_seoul_hospital["위도"].mean()
df_seoul_hospital["경도"].mean()
map = folium.Map(location=[df_seoul_hospital["위도"].mean() , df_seoul_hospital["경도"].mean()],
                 zoom_start=12)

for n in df_seoul_hospital.index:
    name = df_seoul_hospital.loc[n,"상호명"]
    address = df_seoul_hospital.loc[n, "도로명주소"]
    popupp = {name}-{address}
    # popupp = f"{name}-{address}"
    location = [df_seoul_hospital.loc[n,"위도"]  , df_seoul_hospital.loc[n,"경도"]]
    folium.Marker(
        location = location,
        popup = popupp,
    ).add_to(map)
map.save("map.html")
print("완료")


