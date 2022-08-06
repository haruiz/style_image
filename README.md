## Style_Image

This simple python package takes two images, the style image, and the content image, and performs style transfer. It was created to explain how to build python packages using poetry.

`style_image` uses the `magenta/arbitrary-image-stylization-v1-256` model under the hood available in TensorflowHub.

 To get more info about the model check this link : [magenta/arbitrary-image-stylization-v1-256](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2)
### Installation

To install the package, run the following command:

```bash
pip install style_image
```

You can use `style_image` from the command line or using the python API.

### use in the terminal

For running `style_image` from the terminal, run the command below.
```bash
style_image -s picasso_violin -c /Users/haruiz/style_image/data/content_image.jpg -sz 800
```
To get more information about the parameters that need to be provided, run the command `style_image --help`. 

### Use from code
 
```python
from style_image import StyleImage

if __name__ == "__main__":

    content_image_path = "data/content_image.jpg"
    style_image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"

    stylized_image = (
        StyleImage(style_image_path)
        .transfer(content_image_path, output_image_size=800)
        .save("stylized_image.jpg")
    )
```
