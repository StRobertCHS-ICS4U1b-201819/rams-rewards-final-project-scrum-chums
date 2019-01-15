from PIL import Image

image = Image.open('qrcode_test1.jpg')
image.show()

user_codes = {'code': 'qrcode_test1.jpg'}
filename = user_codes['code']

with open(filename, 'rb') as f:
    image = f.read()


