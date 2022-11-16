from streamlit import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

write("# Demo DashBoard")

menu = ["Introduction", "DashBoardDemo"]
choice = sidebar.selectbox('Menu', menu)
if choice=='Introduction':
  subheader("Business Introduction")
  subheader('Load DataFrame: ')
  uploaded_file = file_uploader("Choose a file")


elif choice=='DashBoardDemo':
  subheader('Demo Dashboard Of Revenue')
  subheader('Data Description:')
  text('This dataset is raw data from My company. We support goods express deliver service.')
  df = pd.read_excel(uploaded_file)
  dataframe(df.head())
  
  write("# Number of orders counted by Trạng thái")
  count_TrangThai = df[['Trạng Thái', 'Thu Hộ']].groupby(['Trạng Thái']).count()
  bar_chart(count_TrangThai)
  
  write("# Relationship between KhoiLuong And Revenue")
  fig, ax = plt.subplots()
  ax = sns.scatterplot(data=df, x='Khối Lượng', y='Thu Hộ')

  pyplot(fig)
  
  write("# Revenue based on Trạng Thái")
  fig2 = plt.figure(figsize=(20,10))
  plt.subplot(121)
  sns.barplot(data=df.groupby('Tên Shop').sum().sort_values(by='Khối Lượng').reset_index().head(20), y='Tên Shop', x='Khối Lượng', palette='Blues')
  plt.subplot(122)
  sns.barplot(data=df.groupby('Tên Shop').sum().sort_values(by='Thu Hộ').reset_index().head(20), y='Tên Shop', x='Thu Hộ', palette='Blues')
  plt.tight_layout()
  
  pyplot(fig2)
  
  
  
                                    
  
              
                                    
                                    
  
                           







