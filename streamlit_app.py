import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('my parent new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bluebarry oatmeal')
streamlit.text('🥗kale,spinch & Rocket smoothie')
streamlit.text(' 🐔 Hard boiled free range agg ')
streamlit.text('🥑🍞 Avocado,Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
#streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
#fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/+ this_fruit_choice")
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
   
except URLError as e:
  streamlit.error()

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/fruit_choice")
#streamlit.write('The user entered ', fruit_choice)
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)
#streamlit.stop()
streamlit.header("View our fruit list-Add your favorits!")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()
if streamlit.button('Get fruit list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('from streamlit')")
    return "Thanks for adding" +" "+ new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
