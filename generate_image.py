import json
from PIL import Image, ImageDraw, ImageFont

def load_vocab_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def generate_image(vocab, output_path, text_color="black", bg_color="white"):
    # Create a blank white image
    width, height = 1920, 1080
    image = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(image)

    # Define font and positions
    font_path = "TsunagiGothic.ttf"  # Path to a .ttf font file
    font_large = ImageFont.truetype(font_path, 80)
    font_medium = ImageFont.truetype(font_path, 50)
    font_small = ImageFont.truetype(font_path, 40)

    kanji = vocab["kanji"]
    readings = ", ".join(vocab["readings"])
    meaning = vocab["meaning"]

    # Calculate text size and position
    kanji_bbox = draw.textbbox((0, 0), kanji, font=font_large)
    readings_bbox = draw.textbbox((0, 0), readings, font=font_medium)
    meaning_bbox = draw.textbbox((0, 0), meaning, font=font_small)

    kanji_width, kanji_height = kanji_bbox[2] - kanji_bbox[0], kanji_bbox[3] - kanji_bbox[1]
    readings_width, readings_height = readings_bbox[2] - readings_bbox[0], readings_bbox[3] - readings_bbox[1]
    meaning_width, meaning_height = meaning_bbox[2] - meaning_bbox[0], meaning_bbox[3] - meaning_bbox[1]

    kanji_position = ((width - kanji_width) / 2, (height - kanji_height) / 2 - 100)
    readings_position = ((width - readings_width) / 2, kanji_position[1] + kanji_height + 20)
    meaning_position = ((width - meaning_width) / 2, readings_position[1] + readings_height + 20)

    # Draw the text on the image
    draw.text(kanji_position, kanji, fill=text_color, font=font_large)
    draw.text(readings_position, readings, fill=text_color, font=font_medium)
    draw.text(meaning_position, meaning, fill=text_color, font=font_small)

    # Save the image
    image.save(output_path, format='JPEG')

if __name__ == "__main__":
    vocab_list = load_vocab_from_json("data/vocab.json")
    # Pick a vocab item to display
    generate_image(vocab_list[0], "backgrounds/japstudy_bg.jpg")
