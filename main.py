from style_image import StyleImage

if __name__ == "__main__":

    content_image_path = "data/content_image.jpg"
    style_image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"

    stylized_image = (
        StyleImage(style_image_path)
        .transfer(content_image_path, output_image_size=800)
        .save("stylized_image.jpg")
    )
