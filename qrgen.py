import qrcode.image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

def qrgen(addr, target_dir, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(addr)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{target_dir}/{file_name}.png")

def add_text(addr, target_dir, file_name):
    img = Image.open(f'{target_dir}/{file_name}.png')
    width, height = img.size
    width_2 = width - (width-40)
    height_2 = height - 30
    I1 = ImageDraw.Draw(img)

    font_macos = '/System/Library/Fonts/Supplemental/Courier New.ttf'
    font_ubuntu = '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf'
    font_to_use = ''

    if os.path.exists(font_ubuntu):
        font_to_use = font_ubuntu
    elif os.path.exists(font_macos):
        font_to_use = font_macos
    else:
        print('Ups, defined fonts are not available:')
        print(font_ubuntu)
        print(font_macos)
        exit(0)

    font = ImageFont.truetype(font_to_use, 20)
    I1.text((width_2, height_2), addr, font=font, fill="black")
    img.save(f'{target_dir}/{file_name}.png')

target_dir = 'build/qr'
source_file = 'links.csv'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

if not os.path.exists(source_file):
    with open(source_file, 'w') as f:
        f.write('dakr.link')
        f.write(os.linesep)
        f.write('damiankrawczyk.com')

with open(source_file, 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        addr = line
        file_name = line.replace('.', '-').replace('/', '-')
        qrgen(addr, target_dir, file_name)
        add_text(addr, target_dir, file_name)