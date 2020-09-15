import shutil
import csv
from config import create_config, load_config
from preprocess import preprocess, organize
from keras_train import train
import os


def run():
    with open('models.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        # print(header)
        for row in reader:
            args = dict(zip(header, row))
            model_name = args['model_name']
            # print(model_name)
            if os.path.exists('models/{}/config.json'.format(model_name)):
                args = load_config('models/{}/config.json'.format(model_name))
            else:
                create_config(args)
            preprocess(args)
            organize(args)
            print("-------- training --------")
            train(args)


if os.path.isdir("./baseline"):
    shutil.rmtree("./baseline")
    print("deleted the directory baseline")
if os.path.isdir("./models"):
    shutil.rmtree("./models")
    print("deleted the directory models")

run()
