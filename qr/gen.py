import qrcode.image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def qrgen(addr, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(addr)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{file_name}.png")

def add_text(addr, file_name):
    img = Image.open(f'{file_name}.png')
    width, height = img.size
    width_2 = width - (width-40)
    height_2 = height - 30
    I1 = ImageDraw.Draw(img)
    font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 20)
    I1.text((width_2, height_2), addr, font=font, fill="black")
    img.save(f'{file_name}.png')

with open("links.csv") as f:
    lines = f.read().splitlines()
    for line in lines:
        addr = line
        file_name = line.replace('.', '-').replace('/', '-')
        qrgen(addr, file_name)
        add_text(addr, file_name)