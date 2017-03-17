import sys
from PIL import Image

image = Image.open("map_test.bmp").convert('RGB')

# with open('map_test.bmp', 'rb') as f:
#     image = bytearray(f.read())
# image = misc.imread(os.path.join('map_test.bmp'), flatten=0)
print(image)
