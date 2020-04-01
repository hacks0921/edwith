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
# sns.set(font_scale=1.5, font="AppleGothic") # 그래프 폰트 크기 형태 변경
# print(df_sample.shape)
print(df.columns)

★★★★★★★★★범주형 데이터★★★★★★★★★★

■■■■■ countplot : 빈도수 그림
sns.countplot(x ="음주여부",data= df_sample)
sns.countplot(x ="음주여부",data= df_sample, hue="성별코드") # 축설정, 범주 설정
sns.countplot(x ="연령대코드(5세단위)",data= df_sample, hue="음주여부") # 축설정, 범주 설정
sns.countplot(data=df, x="체중(5Kg단위)", hue="음주여부")

■■■■■ barplot 세로축 막대 그래프 (평균 데이터)
sns.barplot(data=df, x="연령대코드(5세단위)", y="총콜레스테롤")
sns.barplot(data=df, x="연령대코드(5세단위)", y="총콜레스테롤", hue="음주여부")
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤", hue="흡연상태")
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", ci=95)
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", ci=sd)  #표준 편차
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="체중(5Kg 단위)", hue="성별코드", ci=None) # 신뢰구간 미표기

■■■■■ lineplot 꺽은선 그래프
sns.lineplot(data=df, x="연령대코드(5세단위)", y="체중(5Kg 단위)", hue="성별코드")
sns.lineplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="성별코드", ci="sd")
sns.lineplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")

■■■■■ pointplot 점을 포함한 꺽은선 그래프
sns.pointplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")

■■■■■ barplot+ pointplot 점을 포함한 꺽은선 그래프
sns.barplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")
sns.pointplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")
sns.pointplot(data=df, x="연령대코드(5세단위)", y="혈색소", ci=None)

■■■■■ boxplot 그래프
sns.boxplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)")
sns.boxplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="성별코드")
sns.boxplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")

■■■■■ violinplot 그래프
sns.violinplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)")
sns.violinplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
sns.violinplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부", split=True)
sns.violinplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", split=True)

■■■■■ warm plot 그래프
sns.swarmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
sns.swarmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
sns.violinplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)")
sns.swarmplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부")

■■■■■ Implot 그래프  # 회귀선을 볼수 있다  #col 구분하여 표를 나눠서 그릴수 있다
sns.lmplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부")
sns.lmplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", col="성별코드")

★★★★★★★★★수치형 데이터★★★★★★★★★★
■■■■■ scatterplot 그래프 X,Y 수치형 데이터
sns.scatterplot(data=df, x="(혈청지오티)AST", y="(혈청지오티)ALT")
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부")
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="허리둘레")
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", size="체중(5Kg 단위)") # Size를 구분하여 작성가능

■■■■■ implot 그래프    # 상관성을 더 잘 볼수가 있다  그리드처럼 격자로 나옵니다. categorical 데이터로 인식하기 때문입니다
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="성별코드", col="음주여부")
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부", col="성별코드")
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="흡연여부", col="음주여부")
sns.lmplot(data=df_sample, x="수축기혈압", y="이완기혈압", hue="음주여부")
sns.lmplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT")
sns.lmplot(data=df_sample, x="(혈청지오티)AST", y="음주여부")
sns.lmplot(data=df_sample, x="(혈청지오티)AST", y="음주여부", robust=True) # robust 옵션 이상치를 뺴고 그린다


df_chol = df.loc[df["총콜레스테롤"].notnull(), "총콜레스테롤"]


# 이상치 다루기
df_ASLT = df_sample[(df_sample["(혈청지오티)AST"] < 400) & (df_sample["(혈청지오티)ALT"] < 400)]
sns.lmplot(data=df_ASLT, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", ci=None)
df_ASLT_high = df_sample[(df["(혈청지오티)AST"] > 400) | (df["(혈청지오티)ALT"] > 400)]
sns.lmplot(data=df_ASLT_high, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", ci=None)
df_ASLT_high_8000 = df_ASLT_high[df_ASLT_high["(혈청지오티)AST"] > 8000]
df_ASLT_high_8000.iloc[:, 10:27]

plt.show()

print("완료")

