## CropChronicle Prediction API
This repository contains the trained model and prediction API for the CropChronicle project linked at [CropChronicle](https://github.com/DepthPixels/CropChronicle).

### The Model
The Model is a TensorFlow model trained on OpenMeteo data from 15 regions of India to produce results accurate to the zone the input locaiton is in due to the large difference in climate between the zones.

Testing and Model creation was done locally initially but later moved to Google Colab to take advantage of the TPU's faster model compiling speed.
Parameters used from the historical weather data were extensively selected and tweaked to ensure the most accurate results in predictions.
Afterwards the model was exprted as a .keras and this api was created to make predictions.
