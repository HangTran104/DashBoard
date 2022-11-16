from streamlit import *
from plotly.express import *

title('Demo DashBoard')

menu = ["Introduction", "DashBoardDemo"]
choice = sidebar.selectbox('Menu', menu)
if choice=='DataIntroduction':
  subheader("Business Introduction")
elif choice=='DashBoardDemo':
  subheader('Demo Dashboard Of Revenue')

subheader('Load DataFrame: ')
uploaded_file = file_uploader("Choose a file")
subheader('Data Description:')



