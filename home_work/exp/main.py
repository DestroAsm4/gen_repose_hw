import json
import requests
from PIL import Image, ImageDraw

img = Image.new('RGB', (780, 340), 'white')
draw = ImageDraw.Draw(img)

data = '1101110001101011000111111'

for x in range(5):
    for y in range(5):
        if data[x + y * 5] == '1':
            draw.rectangle((x * 10, y * 10, x * 10 + 9, y * 10 + 9), fill='black')
        # if data[x] == '1':
        #   draw.rectangle((x, y, x, y), fill ='black')

img



def jsonkeeper():
    json_data_req = requests.get("https://www.jsonkeeper.com/b/6F42")
    print(json_data_req.status_code)


