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

■■■■■상관계수 구하기■■■■■
columns = ['연령대코드(5세단위)',"혈색소",'음주여부','체중(5Kg단위)','허리둘레', '시력(좌)', '시력(우)', '청력(좌)', '청력(우)', '수축기혈압']
df_small = df_sample[columns]
df_corr = df_small.corr() # 상관계수 구함  # metho에 피어슨,스피어만 등등 정할수있음
print(df_corr)

df_corr["체중(5Kg단위)"].sort_values()
df_corr.loc[df_corr["허리둘레"] > 0.3, "허리둘레"] # 허리둘레와 상관계수가 0.3이상인 feature만 가지고옴

df_corr.loc[df_corr["음주여부"] > 0.1, "음주여부"]
df_corr["혈색소"].sort_values(ascending=False).head(7)

■■■■■heatmap 그리기■■■■■
plt.figure(figsize=(20,7))
mask = np.triu(np.ones_like(df_corr, dtype=np.bool))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="Blues", mask=mask)
# annot 숫자 표시 여부 , fmt 표시 형식, camp 색상, mask 하부만 나오도록 설정 mask는 df_corr로 설정
plt.show()
