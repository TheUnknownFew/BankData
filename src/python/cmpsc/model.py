import pickle
from typing import Dict

import keras as keras
import pandas as pd

from python.cmpsc import pathing
from python.cmpsc.pathing import data_dir

_MO_INDEX = 8
_DOW_INDEX = 9
_PRED_INDEX = 20


def get_encoding_dict():
    with open(pathing.get(pathing.data_dir, 'encodingDict.pkl'), 'rb') as f:
        return pickle.load(f)


example_data = pd.read_csv(pathing.get(data_dir, 'example_data'))
model = keras.models.load_model(pathing.get(data_dir, 'finalmodel'))
mean = pd.read_csv(pathing.get(data_dir, 'mean')).drop([_MO_INDEX, _DOW_INDEX, _PRED_INDEX], axis=0).values.T
std = pd.read_csv(pathing.get(data_dir, 'std')).drop([_MO_INDEX, _DOW_INDEX, _PRED_INDEX], axis=0).values.T
encoding_dict = get_encoding_dict()


def run_example():
    """
    Runs an example data set against the model.
    :return: Prints the results of the example data set.
    """
    example_x = normalize(example_data.drop(['month', 'day_of_week', 'y'], axis=1).replace(to_replace=encoding_dict))
    print(model.predict(example_x))


def normalize(df: pd.DataFrame):
    return (df - mean) / std


def make_prediction(json: Dict):
    """
    Makes a prediction based on the data passed to it.
    :param json: The data with features corresponding to model inputs.
    :return: Returns a prediction from the model.
    1 -> Data entails likely to subscribe : 0 -> Data entails unlikely to subscribe
    """
    client_data = pd.DataFrame([json], index=[0])\
        .astype(example_data.dtypes.drop(['y']).to_dict())\
        .drop(['month', 'day_of_week'], axis=1)\
        .replace(to_replace=encoding_dict)
    return 1 if model.predict(normalize(client_data))[0][0] > 0.5 else 0


if __name__ == '__main__':
    run_example()
