import openmeteo_requests
import datetime

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"

def get_historical_data(in_lat: float, in_long: float):
  end_date = datetime.datetime.now().date() - datetime.timedelta(days=4)
  start_date = end_date - datetime.timedelta(days=29)
  
  params = {
    "latitude": in_lat,
    "longitude": in_long,
    "start_date": str(start_date),
    "end_date": str(end_date),
    "hourly": ["temperature_2m", "precipitation", "surface_pressure", "cloud_cover", "et0_fao_evapotranspiration", "vapour_pressure_deficit", "wind_speed_10m", "sunshine_duration", "shortwave_radiation"],
    "timezone": "auto"
  }
  responses = openmeteo.weather_api(url, params=params)

  # Process first location. Add a for-loop for multiple locations or weather models
  response = responses[0]

  # Process hourly data. The order of variables needs to be the same as requested.
  hourly = response.Hourly()
  hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
  hourly_precipitation = hourly.Variables(1).ValuesAsNumpy()
  hourly_surface_pressure = hourly.Variables(2).ValuesAsNumpy()
  hourly_cloud_cover = hourly.Variables(3).ValuesAsNumpy()
  hourly_et0_fao_evapotranspiration = hourly.Variables(4).ValuesAsNumpy()
  hourly_vapour_pressure_deficit = hourly.Variables(5).ValuesAsNumpy()
  hourly_wind_speed_10m = hourly.Variables(6).ValuesAsNumpy()
  hourly_sunshine_duration = hourly.Variables(7).ValuesAsNumpy()
  hourly_shortwave_radiation = hourly.Variables(8).ValuesAsNumpy()

  hourly_data = {"date": pd.date_range(
    start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
    end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
    freq = pd.Timedelta(seconds = hourly.Interval()),
    inclusive = "left"
  )}
  hourly_data["temperature_2m"] = hourly_temperature_2m
  hourly_data["precipitation"] = hourly_precipitation
  hourly_data["surface_pressure"] = hourly_surface_pressure
  hourly_data["cloud_cover"] = hourly_cloud_cover
  hourly_data["et0_fao_evapotranspiration"] = hourly_et0_fao_evapotranspiration
  hourly_data["vapour_pressure_deficit"] = hourly_vapour_pressure_deficit
  hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
  hourly_data["sunshine_duration"] = hourly_sunshine_duration
  hourly_data["shortwave_radiation"] = hourly_shortwave_radiation

  hourly_dataframe = pd.DataFrame(data = hourly_data)
  return hourly_dataframe