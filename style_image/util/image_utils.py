import functools
import tensorflow as tf
import os
import validators


class ImageUtils:
    @staticmethod
    def crop_center(image):
        """Returns a cropped square image."""
        shape = image.shape
        new_shape = min(shape[1], shape[2])
        offset_y = max(shape[1] - shape[2], 0) // 2
        offset_x = max(shape[2] - shape[1], 0) // 2
        image = tf.image.crop_to_bounding_box(
            image, offset_y, offset_x, new_shape, new_shape
        )
        return image

    @classmethod
    @functools.lru_cache(maxsize=None)
    def load_image(cls, image_path, image_size=(256, 256), preserve_aspect_ratio=True):
        """Loads and preprocesses images."""
        # Cache image file locally.
        if validators.url(image_path):
            image_path = tf.keras.utils.get_file(
                os.path.basename(image_path)[-128:], image_path
            )
        # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
        img = tf.io.decode_image(
            tf.io.read_file(image_path), channels=3, dtype=tf.float32
        )[tf.newaxis, ...]
        img = cls.crop_center(img)
        img = tf.image.resize(
            img, image_size, preserve_aspect_ratio=preserve_aspect_ratio
        )
        return img
