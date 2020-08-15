import csv
from config import create_config, load_config
from preprocess import preprocess, organize
from keras_train import train
import os

with open('models.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    # print(header)
    for row in reader:
        args = dict(zip(header, row))
        model_name = args['model_name']
        print(model_name)
        if os.path.exists('models/{}/config.json'.format(model_name)):
            args = load_config('models/{}/config.json'.format(model_name))
        else:
            create_config(args)
        preprocess(args)
        organize(args)
        train(args)
