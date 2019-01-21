from PIL import Image

image = Image.open('code.png')
image.show()

user_codes = {'code': 'code.png'}
filename = user_codes['code']

with open(filename, 'code') as f:
    image = f.read()


