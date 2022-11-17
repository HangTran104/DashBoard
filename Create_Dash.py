from streamlit import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

write("# Demo DashBoard")
uploaded_file = file_uploader("Choose a file")

menu = ["Introduction", "DashBoardDemo"]
choice = sidebar.selectbox('Menu', menu)
if choice=='Introduction':
  subheader("Business Introduction")
  
  


elif choice=='DashBoardDemo':
  subheader('Demo Dashboard Of Revenue')
  subheader('Data Description:')
  text('This dataset is raw data from My company. We support goods express deliver service.')
  subheader('Load DataFrame: ')
  df = pd.read_excel(uploaded_file)
  dataframe(df.head())
 
  
  
  write("# Number of orders counted by Trạng thái")
  count_TrangThai = df[['Trạng Thái', 'Thu Hộ']].groupby(['Trạng Thái']).count()
  bar_chart(count_TrangThai)
  
  write("# Relationship between KhoiLuong And Revenue")
  fig, ax = plt.subplots()
  ax = sns.swarmplot(data=df, x='Trạng Thái', y='Thu Hộ')
  plt.xticks(rotation=90)

  pyplot(fig)
  
  
  write("# Revenue based on Trạng Thái")
  status = multiselect("Status", options=df['Trạng Thái'].unique())
  submit = button('Submit')
  write(type(status))
  
#   df_plot=pd.DataFrame(columns=df.columns)
#   for i in range(len(status)):
#     filtered_df = df[df["Trạng Thái"].isin(status)]
#     df_plot=pd.concat(df_plot,filtered_df )
  
  
 
  fig2 = plt.figure(figsize=(20,10))
  plt.subplot(121)
  sns.barplot(data=df_plot.groupby('Tên Shop').sum().sort_values(by='Khối Lượng', ascending=False).reset_index().head(20), y='Tên Shop', x='Khối Lượng', palette='Blues')
  plt.subplot(122)
  sns.barplot(data=df_plot.groupby('Tên Shop').sum().sort_values(by='Thu Hộ', ascending=False).reset_index().head(20), y='Tên Shop', x='Thu Hộ', palette='Blues')
  plt.tight_layout()                               
#   fig2 = plt.figure(figsize=(20,10))
#   plt.subplot(121)
#   sns.barplot(data=df[df['Trạng Thái']==status].groupby('Tên Shop').sum().sort_values(by='Khối Lượng', ascending=False).reset_index().head(20), y='Tên Shop', x='Khối Lượng', palette='Blues')
#   plt.subplot(122)
#   sns.barplot(data=df[df['Trạng Thái']==status].groupby('Tên Shop').sum().sort_values(by='Thu Hộ', ascending=False).reset_index().head(20), y='Tên Shop', x='Thu Hộ', palette='Blues')
#   plt.tight_layout()
                                   
  
  pyplot(fig2)
  
  
  
                                    
  
              
                                    
                                    
  
                           







