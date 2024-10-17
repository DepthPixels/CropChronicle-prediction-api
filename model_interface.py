import pandas as pd
import tensorflow as tf
from helpers import shape_dataset, find_zone

from data_collector import get_historical_data


feature_keys = [
  "temperature_2m",
  "precipitation",
  "surface_pressure",
  "cloud_cover",
  "et0_fao_evapotranspiration",
  "vapour_pressure_deficit",
  "wind_speed_10m",
  "shortwave_radiation",
  "sunshine_duration"
]


zone_list = ['Western Himalayan',
             'Western Plain',
             'Lower Gangetic Plains',
             'Middle Gangetic Plains',
             'Upper Gangetic Plains',
             'Trans-Gangetic Plains',
             'Eastern Plateau & Hills',
             'Central Plateau & Hills',
             'Western Plateau & Hills',
             'Southern Plateau & Hills',
             'East Coast Plains & Hills',
             'West Coast Plains & Hills',
             'Gujarat Plains & Hills',
             'Western Dry Region',
             'Islands']

date_time_key = "date"

def make_predictions(in_lat, in_long):
  
  zone = zone_list.index(find_zone(in_lat, in_long)) + 1
  df = get_historical_data(in_lat, in_long)
  
  cc = df['cloud_cover']
  bad_cc = cc < 0
  bad2_cc = cc > 100
  cc[bad_cc] = 0
  cc[bad2_cc] = 100
  
  features = df[feature_keys]
  features.index = df[date_time_key]
  features = features.dropna()
  features_values = features.values
  
  model = tf.keras.models.load_model(f'./models/zone_{zone}_model_f.keras')
  
  inputs = tf.keras.preprocessing.timeseries_dataset_from_array(
    data=features_values,
    targets=None,
    sequence_length=720,
    batch_size=32
  )
  inputs = inputs.map(shape_dataset)
  outputs = model.predict(inputs.take(1))
    
  return outputs


def predict_yield(crop_type):
  df = pd.read_csv('./final_yields.csv')
  df.index = df['Crop']
  output = df.loc[crop_type].iloc[1]
  
  return output

def irrigation_data(latitude, longitude):
  predictions = make_predictions(latitude, longitude)
  evapo = predictions[:, :, 4]
  precip = predictions[:, :, 1]
  irrigation = evapo - precip
  return irrigation[0, :]