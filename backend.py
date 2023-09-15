import requests

API_key="d8bc42dc80f81f79dad21e906dd80c6c"

def get_data(place,forecast_days):
    url=(f"https://api.openweathermap.org/data/2.5/forecast?"
         f"q={place}&"
         f"appid={API_key}")
    request=requests.get(url)
    content=request.json()
    filtered_data=content["list"]
    nr_values=forecast_days*8
    filtered_data=filtered_data[:nr_values]
    return filtered_data

# if __name__=="__main__":
#    print(get_data("london",3))