import tensorflow as tf
import numpy as np
import os

with open('app/class_names.txt') as temp_file:
    class_list = [line.rstrip('\n') for line in temp_file]

similar = {'Monaco': 'Indonesia', 'Romania': 'Chad',
           'Chad': 'Romania', 'Indonesia': 'Monaco'}


def predict_flag_file(new_img_path: str, model: tf.keras.models.Sequential,
                      img_height: int = 180, img_width: int = 240) -> str:
    '''Predicts a country label on a given image'''
    img = tf.keras.utils.load_img(
        new_img_path, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    predictions = model.predict(img_array)
    return class_list[np.argmax(predictions)]


def predict_on_folder(model: tf.keras.models.Sequential,
                      origin_dir: str = './download_flags_2/',
                      verbose: bool = True) -> float:
    '''
    Predicts a country labels on images in a given dir. 
    If verbose is True prints the ones that where mispredicted.
    Returns a fraction of the mispredicted values.
    '''
    os.chdir(origin_dir)
    count_all = 0
    count_wrong = 0
    for flag_name in os.listdir('./'):
        os.chdir(flag_name)

        for flag_file in os.listdir('./'):
            pred = predict_flag_file(flag_file, model)
            flag_n = flag_name.replace(' flag', '')
            if pred != flag_n:
                if pred not in similar and similar.get(pred) != flag_n:
                    count_wrong += 1
                    if verbose:
                        print(f'{pred} - {flag_file} - {flag_name}')
            count_all += 1
        os.chdir('..')
    os.chdir('..')
    return count_wrong/count_all
