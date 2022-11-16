from streamlit import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.markdown("<h1 style='color:red'>Demo DashBoard</h1>")

menu = ["Introduction", "DashBoardDemo"]
choice = sidebar.selectbox('Menu', menu)
if choice=='DataIntroduction':
  subheader("Business Introduction")
elif choice=='DashBoardDemo':
  subheader('Demo Dashboard Of Revenue')

subheader('Load DataFrame: ')
uploaded_file = file_uploader("Choose a file")
subheader('Data Description:')
text('This dataset is raw data from My company. We support goods express deliver service.')

df = pd.read_excel(uploaded_file)
dataframe(df.head())

st.write("<h4 style='color:blue; font-weight:bold'>Relationship between KhoiLuong And Revenue</h4>")
count_TrangThai = df[['Trạng Thái', 'Thu Hộ']].groupby(['Trạng Thái']).count()
bar_chart(count_TrangThai)

fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, x='Khối Lượng', y='Thu Hộ')

pyplot(fig)



