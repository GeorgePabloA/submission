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
ax.set_title("Temperature in Celcius", loc="center", fontsize=12, font='Times New Roman')
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
ax.set_title("Temperature in Celcius", loc="center", fontsize=12, font='Times New Roman')
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
ax.set_title("Temperature in Celcius", loc="center", fontsize=12, font='Times New Roman')

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
ax.set_title("Temperature in Celcius", loc="center", fontsize=12, font='Times New Roman')

st.pyplot(fig)

st.text("""Here are the highest humidity data along with the climate that affects bike rentals.""")

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 6))

x = np.arange(len(all_df["season"]))[:len(all_df["season"])//2]
width = 0.4

casual = axs[0].plot(x, all_df["casual"][:len(all_df["casual"])//2], label='casual', linestyle='-', color='steelblue')
axs[0].set_title(None, size=16)
axs[0].set_ylabel('Total Casual Customers', size=14)
axs[0].set_xticks(x)
axs[0].legend(fontsize=14)

registered = axs[1].plot(x, all_df["registered"][:len(all_df["registered"])//2], label='registered', linestyle='-', color='lightcoral')
axs[1].set_title(None, size=16)
axs[1].set_ylabel('Total Registered Customers', size=14)
axs[1].set_xticks(x)
axs[1].legend(fontsize=14)

st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """This is half the data that I can get out and am still trying to develop the data.
        """
    )


text = st.text_area('Leave feedback to make us better')
st.write('Feedback: ', text)
