from PIL import Image, ImageOps
import os

counter = 0

for filename in os.listdir('input_images'):
    clean_name = os.path.splitext(filename)[0]
    image = Image.open(f'input_images/{filename}')
    if image.size[0] != image.size[1]:
        img = ImageOps.pad(image, (400, 400), Image.ANTIALIAS, color=(255, 255, 255))
    else:
        img = ImageOps.pad(image, (400, 400), Image.ANTIALIAS)
    img.save(f'output_images/{clean_name}.png', 'png')
    counter += 1
    counter_res = counter

print(f'{counter_res} files converted')
