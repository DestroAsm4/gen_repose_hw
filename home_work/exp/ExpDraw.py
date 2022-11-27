from PIL import Image, ImageDraw

img = Image.new('RGB', (780, 340), 'white')
draw = ImageDraw.Draw(img)

data = '1101110001101011000111111'

# for x in range(5):
#     for y in range(5):
#         if data[x + y * 5] == '1':
#             draw.rectangle((x * 10, y * 10, x * 10 + 9, y * 10 + 9), fill ='black')

# код берет первый и каждый пятый элемент, если этот элемент 1 он рисует
# квадратик (x, y , x, y) ?не знаю зачем усложнять и брать каждый 5 элемент,
# а не написать все по порядку? - ответ: так оно рисуется в порядке с верху вниз по y

x = 2
y = 1
# for i in data:
#       if i == '1':
#         draw.rectangle((x * 10, y * 10, x * 10 + 20, y * 10 + 20), fill ='black')

# draw.rectangle((x * 10, y * 10, x * 10 + 9, y * 10 + 9), fill ='black')

img.show()