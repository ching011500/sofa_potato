import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 顏色與風格設定
colors = ['#FF9999', '#99CCFF', '#FFCC99']
palette = ['#FF9999', '#99CCFF']

# 繁體中文設定
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 標題
st.title("敘述統計與視覺化分析")

# 讀取整理後的資料
data_path = "/Users/yuchingchen/Documents/大三/實設/期末/試算表 ID - 工作表1.csv"
df = pd.read_csv(data_path)

# 新增欄位名稱並刪除最後一欄
df.columns = ['性別', '題目', '分數', '刪除欄位']
df = df.drop(columns=['刪除欄位'])

# 將第一列變成第二列，並從指定資料開始
df_new = pd.DataFrame([['女性', '題目 1', 10]], columns=['性別', '題目', '分數'])
df = pd.concat([df_new, df], ignore_index=True)
df['分數'] = pd.to_numeric(df['分數'], errors='coerce')

# 顯示整理後的資料
st.subheader("整理後的資料")
st.dataframe(df)

# 基本敘述統計
st.write("## 基本敘述統計")
st.write("### 整體分數的統計資訊")
st.dataframe(df['分數'].describe())

# 性別分組統計
st.write("## 按性別分組的統計資訊")
gender_stats = df.groupby('性別')['分數'].describe()
st.dataframe(gender_stats)

# 題目分組統計
st.write("## 按題目分組的統計資訊")
topic_stats = df.groupby('題目')['分數'].describe()
st.dataframe(topic_stats)

# 交叉統計 (性別 x 題目)
st.write("## 性別與題目的交叉統計")
cross_stats = df.groupby(['性別', '題目'])['分數'].describe()
st.dataframe(cross_stats)

# 分數分布直方圖
st.write("## 分數分布直方圖")
fig, ax = plt.subplots(figsize=(8, 6))
plt.hist(df['分數'], bins=10, edgecolor='black', color=colors[0])
plt.title('分數分布直方圖', fontsize=14)
plt.xlabel('分數', fontsize=12)
plt.ylabel('次數', fontsize=12)
plt.grid(axis='y', alpha=0.5)
st.pyplot(fig)  # 使用 st.pyplot() 顯示圖表

# 箱型圖：性別分數比較
st.write("## 不同性別的分數分布")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='性別', y='分數', data=df, palette=palette, ax=ax)
plt.title('不同性別的分數分布', fontsize=14)
plt.xlabel('性別', fontsize=12)
plt.ylabel('分數', fontsize=12)
st.pyplot(fig)

# 長條圖：性別平均分數比較
st.write("## 不同性別的平均分數")
mean_scores = df.groupby('性別')['分數'].mean()
fig, ax = plt.subplots(figsize=(8, 6))
plt.bar(mean_scores.index, mean_scores.values, color=colors[2], edgecolor='black')
plt.title('不同性別的平均分數', fontsize=14)
plt.xlabel('性別', fontsize=12)
plt.ylabel('平均分數', fontsize=12)
plt.grid(axis='y', alpha=0.5)
st.pyplot(fig)

# 交叉統計視覺化：性別與題目的平均分數
st.write("## 性別與題目的交叉統計 - 平均分數")
cross_stat = df.groupby(['性別', '題目'])['分數'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='題目', y='分數', hue='性別', data=cross_stat, palette=palette, ax=ax)
plt.title('性別與題目的交叉統計 - 平均分數', fontsize=14)
plt.xlabel('題目', fontsize=12)
plt.ylabel('平均分數', fontsize=12)
plt.legend(title='性別')
plt.grid(axis='y', alpha=0.5)
st.pyplot(fig)

# 完成提示
st.write("### 以上是敘述統計與視覺化結果。")
