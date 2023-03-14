import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def preprocess_cars(cars: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for cars.
    Args:
        cars: Raw data.
    Returns:
        Preprocessed cars data.
    """
    df1 = cars.copy()
    df1['model'] = [x.split()[0] for x in df1['CarName']]
    # Fix spelling mistakes in data and abbreviations
    df1['model'] = df1['model'].replace({'maxda': 'Mazda', 'mazda': 'Mazda',
                                         'nissan': 'Nissan',
                                         'porcshce': 'Porsche', 'porsche': 'Porsche',
                                         'toyouta': 'Toyota', 'toyota': 'Toyota',
                                         'vokswagen': 'Volkswagen', 'vw': 'Volkswagen', 'volkswagen': 'Volkswagen'})
    df1 = df1.drop(['car_ID', 'CarName'], axis=1)

    numerical = df1.drop(['price'], axis=1).select_dtypes('number').columns
    categorical = df1.select_dtypes('object').columns

    df1 = df1.drop('citympg', axis=1)

    processed_cars = pd.get_dummies(df1, columns=categorical, drop_first=True)

    return processed_cars
