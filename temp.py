
import streamlit  as st
import requests

API_KEY='45f2ebe4f754218a7cabae477a9c2d69'


def find_Current_Weather(city):
    base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_Data=requests.get(base_url).json()
    # st.json(weather_Data)
    try:
        # general=weather_Data['weather'][0]['main']
        icon_id = weather_Data['weather'][0]['icon']
        temperature = round(weather_Data['main']['temp']-273.15)
        humidty = weather_Data['main']['humidity']
        clouds=weather_Data['clouds']['all']
        # icon=f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("city Not given dataset")
    return temperature,humidty,clouds





if __name__=='__main__':

    pass