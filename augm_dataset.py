import tensorflow as tf
import imageio
import os
import numpy as np


def datagen_gen(shear_range: float = 0.15, zoom_range: float = 0.2,
                channel_shift_range: float = 50,
                brightness_range: tuple[float, float] = (0.6, 1.),
                width_shift_range: float = 0.02,
                height_shift_range: float = 0.02
                ) -> tf.keras.preprocessing.image.ImageDataGenerator:
    """Return tensorflow ImageDataGenerator object with defined augmentation parameters"""

    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        shear_range=shear_range,
        zoom_range=zoom_range,
        channel_shift_range=channel_shift_range,
        brightness_range=brightness_range,
        width_shift_range=width_shift_range,
        height_shift_range=height_shift_range,
    )

    return datagen


def generate_augm_images(origin_dir: str = './flags/', out_dir: str = './augm_flags/',
                         num_augm: int = 100) -> None:
    """Create a folder with generated augmented images

    :param origin_dir: The folder where the origin images are located.
    :param out_dir: The folder where augmented images will be saved.
    :param num_augm: The maximum number of augmented images that will be created.
    """
    for flag_name in os.listdir(origin_dir):
        save_here = f'{out_dir}{flag_name}'
        os.makedirs(save_here, exist_ok=True)

        image_path = f'{origin_dir}{flag_name}/{flag_name}.png'

        image = np.expand_dims(imageio.imread(image_path), 0)

        # Some flags dont have all 3 channels - one more expand is needed
        if len(image.shape) == 3:
            image = np.expand_dims(image, -1)

        datagen = datagen_gen()
        datagen.fit(image)

        # Loop lets save images in dirs
        for x, val in zip(datagen.flow(image,
                                       save_to_dir=save_here,
                                       save_prefix=flag_name,
                                       save_format='png'), range(num_augm)):
            pass


if __name__ == '__main__':
    generate_augm_images(num_augm=1000)
    generate_augm_images(out_dir='./augm_flags_test/')
