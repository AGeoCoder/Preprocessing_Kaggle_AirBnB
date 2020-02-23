# Preprocessing_Kaggle_AirBnB
Preprocessing Data from an AirBnB Dataset from Kaggle

For use with a Kaggle dataset like that from "https://www.kaggle.com/jeploretizo/san-francisco-airbnb-listings/data".

The Kaggle dataset with AirBnB listings has the "Amenities" data all listed in an array inside of one column. However, this isn't ideal if you want to mine the dataset for information using specific amenities as predictor variables. I show an example of how to take data on specific amenities (e.g. Parking) and put them in their own column in a separate CSV file using a simple Python script. (This separate CSV file can then easily be merged with the original CSV file using Excel.)
