import streamlit
streamlit.title('my parent new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bluebarry oatmeal')
streamlit.text('🥗kale,spinch & Rocket smoothie')
streamlit.text(' 🐔 Hard boiled free range agg ')
streamlit.text('🥑🍞 Avocado,Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
