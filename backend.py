import requests

API_KEY = "255273f36f4d7edc6907e6df6d1b5398"


def get_data(place, forecast_days=None, kind=None):
    units = "metric"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=[units]"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Weert", forecast_days=3))
