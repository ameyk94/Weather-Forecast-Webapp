import requests

API_KEY = "0ab6eae08ed5e706351bdf6407a04679"

def get_data(place, forecast_days=None,kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values] # each day has 8 observations
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))