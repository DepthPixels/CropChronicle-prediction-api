import haversine

coordinate_list = [
[34.0837, 74.7973],
[31.1048, 77.1734],
[30.3165, 78.0322],
[34.1526, 77.5771],
[26.9124, 75.7873],
[26.2389, 73.0243],
[28.0229, 73.3119],
[26.4499, 74.6399],
[22.5726, 88.3639],
[27.041, 88.2663],
[23.2324, 87.8615],
[25.0108, 88.1411],
[25.5941, 85.1376],
[25.3176, 82.9739],
[26.8467, 80.9462],
[26.7606, 83.3732],
[28.9845, 77.7064],
[26.4499, 80.3319],
[27.8974, 78.088],
[29.9457, 78.1642],
[30.7333, 76.7794],
[31.634, 74.8723],
[30.9, 75.8573],
[28.4595, 77.0266],
[21.1458, 79.0882],
[21.2514, 81.6296],
[20.2961, 85.8245],
[22.2604, 84.8536],
[23.2599, 77.4126],
[22.7196, 75.8577],
[23.1815, 79.9864],
[26.2183, 78.1828],
[19.076, 72.8777],
[18.5204, 73.8567],
[19.8762, 75.3433],
[19.9975, 73.7898],
[12.9716, 77.5946],
[17.385, 78.4867],
[13.0827, 80.2707],
[12.2958, 76.6394],
[13.0827, 80.2707],
[17.6868, 83.2185],
[11.9416, 79.8083],
[20.4625, 85.8828],
[15.4909, 73.8278],
[12.9141, 74.856],
[16.9902, 73.312],
[8.5241, 76.9366],
[23.0225, 72.5714],
[21.1702, 72.8311],
[22.3039, 70.8022],
[22.3072, 73.1812],
[26.9157, 70.9083],
[25.7453, 71.3921],
[23.241, 69.6669],
[28.0229, 73.3119],
[11.6234, 92.7265],
[12.0722, 92.9827],
[10.5593, 72.6358],
[8.2829, 73.0451]
]

city_list = [
'Srinagar',
'Shimla',
'Dehradun',
'Leh',
'Jaipur',
'Jodhpur',
'Bikaner',
'Ajmer',
'Kolkata',
'Darjeeling',
'Burdwan',
'Malda',
'Patna',
'Varanasi',
'Lucknow',
'Gorakhpur',
'Meerut',
'Kanpur',
'Aligarh',
'Haridwar',
'Chandigarh',
'Amritsar',
'Ludhiana',
'Gurugram',
'Nagpur',
'Raipur',
'Bhubaneswar',
'Rourkela',
'Bhopal',
'Indore',
'Jabalpur',
'Gwalior',
'Mumbai',
'Pune',
'Aurangabad',
'Nashik',
'Bangalore',
'Hyderabad',
'Chennai',
'Mysore',
'Chennai',
'Visakhapatnam',
'Pondicherry',
'Cuttack',
'Panaji',
'Mangalore',
'Ratnagiri',
'Thiruvananthapuram',
'Ahmedabad',
'Surat',
'Rajkot',
'Vadodara',
'Jaisalmer',
'Barmer',
'Bhuj',
'Bikaner',
'Port Blair',
'Havelock Island',
'Kavaratti',
'Minicoy'
]

zone_dict = {'Western Himalayan': ['Srinagar', 'Shimla', 'Dehradun', 'Leh'],
             'Western Plain': ['Jaipur', 'Jodhpur', 'Bikaner', 'Ajmer'],
             'Lower Gangetic Plains': ['Kolkata', 'Darjeeling', 'Burdwan', 'Malda'],
             'Middle Gangetic Plains': ['Patna', 'Varanasi', 'Lucknow', 'Gorakhpur'],
             'Upper Gangetic Plains': ['Meerut', 'Kanpur', 'Aligarh', 'Haridwar'],
             'Trans-Gangetic Plains': ['Chandigarh', 'Amritsar', 'Ludhiana', 'Gurugram'],
             'Eastern Plateau & Hills': ['Nagpur', 'Raipur', 'Bhubaneswar', 'Rourkela'],
             'Central Plateau & Hills': ['Bhopal', 'Indore', 'Jabalpur', 'Gwalior'],
             'Western Plateau & Hills': ['Mumbai', 'Pune', 'Aurangabad', 'Nashik'],
             'Southern Plateau & Hills': ['Bangalore', 'Hyderabad', 'Chennai', 'Mysore'],
             'East Coast Plains & Hills': ['Chennai', 'Visakhapatnam', 'Pondicherry', 'Cuttack'],
             'West Coast Plains & Hills': ['Panaji', 'Mangalore', 'Ratnagiri', 'Thiruvananthapuram'],
             'Gujarat Plains & Hills': ['Ahmedabad', 'Surat', 'Rajkot', 'Vadodara'],
             'Western Dry Region': ['Jaisalmer', 'Barmer', 'Bhuj', 'Bikaner'],
             'Islands': ['Port Blair', 'Havelock Island', 'Kavaratti', 'Minicoy']
}

def find_distance(a1, a2, b1, b2):
  loc1 = (a1, b1)
  loc2 = (a2, b2)
  
  dist = haversine.haversine(loc1, loc2)
  return dist

def shape_dataset(inputs):
  inputs.set_shape([None, 720, None])
  
  return inputs

def find_zone(latitude, longitude):
  length_list = []
  for coordinates in coordinate_list:
    a2, b2 = coordinates
    dist = find_distance(latitude, a2, longitude, b2)
    length_list.append(dist)
    
  min_dist = min(length_list)
  min_index = length_list.index(min_dist)
  closest_city = city_list[min_index]
  for key, value in zone_dict.items():
    if closest_city in value:
      assigned_zone = key
      
  return assigned_zone