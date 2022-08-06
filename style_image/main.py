from style_image import StyleImage
import typer

app = typer.Typer()


def style_image_callback(value: str):
    style_urls = dict(
        kanagawa_great_wave="https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg",
        kandinsky_composition_7="https://upload.wikimedia.org/wikipedia/commons/b/b4/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg",
        hubble_pillars_of_creation="https://upload.wikimedia.org/wikipedia/commons/6/68/Pillars_of_creation_2014_HST_WFC3-UVIS_full-res_denoised.jpg",
        van_gogh_starry_night="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
        turner_nantes="https://upload.wikimedia.org/wikipedia/commons/b/b7/JMW_Turner_-_Nantes_from_the_Ile_Feydeau.jpg",
        munch_scream="https://upload.wikimedia.org/wikipedia/commons/c/c5/Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg",
        picasso_demoiselles_avignon="https://upload.wikimedia.org/wikipedia/en/4/4c/Les_Demoiselles_d%27Avignon.jpg",
        picasso_violin="https://upload.wikimedia.org/wikipedia/en/3/3c/Pablo_Picasso%2C_1911-12%2C_Violon_%28Violin%29%2C_oil_on_canvas%2C_Kr%C3%B6ller-M%C3%BCller_Museum%2C_Otterlo%2C_Netherlands.jpg",
        picasso_bottle_of_rum="https://upload.wikimedia.org/wikipedia/en/7/7f/Pablo_Picasso%2C_1911%2C_Still_Life_with_a_Bottle_of_Rum%2C_oil_on_canvas%2C_61.3_x_50.5_cm%2C_Metropolitan_Museum_of_Art%2C_New_York.jpg",
        fire="https://upload.wikimedia.org/wikipedia/commons/3/36/Large_bonfire.jpg",
        derkovits_woman_head="https://upload.wikimedia.org/wikipedia/commons/0/0d/Derkovits_Gyula_Woman_head_1922.jpg",
        amadeo_style_life="https://upload.wikimedia.org/wikipedia/commons/8/8e/Untitled_%28Still_life%29_%281913%29_-_Amadeo_Souza-Cardoso_%281887-1918%29_%2817385824283%29.jpg",
        derkovtis_talig="https://upload.wikimedia.org/wikipedia/commons/3/37/Derkovits_Gyula_Talig%C3%A1s_1920.jpg",
        amadeo_cardoso="https://upload.wikimedia.org/wikipedia/commons/7/7d/Amadeo_de_Souza-Cardoso%2C_1915_-_Landscape_with_black_figure.jpg",
    )
    if value in style_urls:
        return style_urls[value]
    return value


@app.command()
def main(
    style_image: str = typer.Option(
        ..., "--style_image", "-s", callback=style_image_callback
    ),
    content_image: str = typer.Option(..., "--content_image", "-c"),
    output_image_size: int = typer.Option(384, "--output_image_size", "-sz"),
    output_image_path: str = typer.Option("stylized_image.png", "--output_image_path", "-o"),
):
    style_image = StyleImage(style_image)
    stylized_image = style_image.transfer(content_image, output_image_size=output_image_size)
    stylized_image.save(output_image_path)
