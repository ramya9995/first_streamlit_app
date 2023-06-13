
import streamlit
streamlit.title('My parents new health diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 and blueberry oatmeal')
streamlit.text('🥗kale, spinach and oatmeal')
streamlit.text('🐔 Hard-boiled free-range Egg')
streamlit.text('🥑🍞Acocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
