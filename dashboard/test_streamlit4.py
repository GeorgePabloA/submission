import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

all_df = pd.read_csv("https://raw.githubusercontent.com/GeorgePabloA/submission/main/dashboard/all.csv")

st.title('Belajar Analisis Data')
 
with st.sidebar:
    st.title('This is the sidebar')

    st.image("https://apicms.thestar.com.my/uploads/images/2021/02/24/1055397.jpg")

    st.text('Still under development')

st.title('Bicycle Data')


st.header('Some factors that influence data')


st.subheader('Normalized temperature in Celsius')

temp_yr_df = all_df.groupby("temp").weathersit.nunique().sort_values(ascending=False).reset_index()

temp_yr_df.head(15)
x = np.arange(len(temp_yr_df["temp"]))

fig, ax = plt.subplots(figsize=(12, 6))
 
sns.barplot(x="temp", y="weathersit", data=temp_yr_df.head(10), hue="temp", palette='winter', ax=ax, legend=False)
ax.set_ylabel('Wheater')
ax.set_xlabel('Temperature')
ax.set_title("Temperature in Celcius", loc="center", fontsize=12)
ax.tick_params(axis ='y', labelsize=10)

st.pyplot(fig)

st.text('Here are the highest temperature data along with the climate that affects bike rentals.')


st.subheader('Normalized feeling temperature in Celsius')

temp_yr_df = all_df.groupby("atemp").weathersit.nunique().sort_values(ascending=False).reset_index()

temp_yr_df.head(15)
x = np.arange(len(temp_yr_df["atemp"]))


fig, ax = plt.subplots(figsize=(12, 6))
 
sns.barplot(x="atemp", y="weathersit", data=temp_yr_df.head(10), hue="atemp", palette='winter', ax=ax, legend=False)
ax.set_ylabel('Wheater')
ax.set_xlabel('Temperature')
ax.set_title("Temperature in Celcius", loc="center", fontsize=12)
ax.tick_params(axis ='y', labelsize=10)

st.pyplot(fig)

st.text('Here are the highest temperature data along with the climate that affects bike rentals.')

st.subheader('Normalized humidity')

temp_yr_df = all_df.groupby("hum").weathersit.nunique().sort_values(ascending=False).reset_index()

temp_yr_df.head(15)
x = np.arange(len(temp_yr_df["hum"]))


fig, ax = plt.subplots(figsize=(12, 6))
 
sns.barplot(x="hum", y="weathersit", data=temp_yr_df.head(10), hue="hum", palette='winter', ax=ax, legend=False)
ax.set_ylabel('Wheater')
ax.set_xlabel('Temperature')
ax.set_title("Temperature in Celcius", loc="center", fontsize=12)

st.pyplot(fig)

st.text("""Here are the highest humidity data along with the climate that affects bike rentals.""")

st.subheader('Normalized wind speed')

temp_yr_df = all_df.groupby("windspeed").weathersit.nunique().sort_values(ascending=False).reset_index()

temp_yr_df.head(15)
x = np.arange(len(temp_yr_df["windspeed"]))

fig, ax = plt.subplots(figsize=(12, 6))
 
sns.barplot(x="windspeed", y="weathersit", data=temp_yr_df.head(10), hue="windspeed", palette='winter', ax=ax, legend=False)
ax.set_ylabel('Wheater')
ax.set_xlabel('Windspeed')
ax.set_title("Temperature in Celcius", loc="center", fontsize=12)

st.pyplot(fig)

st.text("""Here are the highest humidity data along with the climate that affects bike rentals.""")

typecst = ['Registered', 'Casual']
values = [all_df['registered'].sum(), all_df['casual'].sum()]
colors = ['#8B4513', '#FFF8DC']
explode = (0.1, 0.1)
 
typecst = ['Registered', 'Casual']
values = [all_df['registered'].sum(), all_df['casual'].sum()]
colors = ['#8B4513', '#FFF8DC']
explode = (0.1, 0.1)

st.title('Casual and Registered Customers')

fig, ax = plt.subplots()
ax.pie(values, labels=typecst, autopct='%1.1f%%', colors=colors, explode=explode)
ax.axis('equal')
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """This is a comparison between casual customers and registered customers. (This data is taken within 2 years.)
        """
    )


text = st.text_area('Leave feedback to make us better')
st.write('Feedback: ', text)
