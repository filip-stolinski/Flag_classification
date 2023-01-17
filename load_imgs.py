import tensorflow as tf
import pathlib


def load_from_dir(dir_path: str = './flags', img_height: int = 180,
                  img_width: int = 240, batch_size: int = 32) -> tf.data.Dataset:
    '''Creates tensorflow dataset that can be used in model.fit'''
    data_dir = pathlib.Path(dir_path).with_suffix('')

    img_dataset = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        labels='inferred',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    return img_dataset
