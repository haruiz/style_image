import tensorflow as tf
import tensorflow_hub as hub

from style_image.util import ImageUtils
from PIL import Image as PILImage


class StyleImage:
    def __init__(self, style_image_path):
        self._style_image_path = style_image_path
        hub_handle = (
            "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
        )
        self._hub_module = hub.load(hub_handle)

    def transfer(
        self, content_image_path, output_image_size=384, style_img_size=(256, 256)
    ):
        """
        transfer the style of the style image to the content image
        :param content_image_path: image path of the content image :
        :param output_image_size: The content image size can be arbitrary.
        :param style_img_size: The style prediction model was trained with image size 256 and it's the
        recommended image size for the style image (though, other sizes work as
        well but will lead to different results).
        Recommended to keep it at 256.
        :return:
        """
        content_img_size = (output_image_size, output_image_size)
        # Load the content and style images.
        content_image = ImageUtils.load_image(content_image_path, content_img_size)
        style_image = ImageUtils.load_image(self._style_image_path, style_img_size)
        # Stylize image.
        stylized_image_tensor = self._hub_module(
            tf.constant(content_image), tf.constant(style_image)
        )[0]
        stylized_image_arr = tf.image.convert_image_dtype(
            stylized_image_tensor, tf.uint8
        ).numpy()
        stylized_image_arr = stylized_image_arr[0]  # Remove batch dimension.
        stylized_image = PILImage.fromarray(stylized_image_arr)
        return stylized_image
