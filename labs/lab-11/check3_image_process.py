
from PIL import Image
from PIL import ImageOps
import numpy as np

shirt = Image.open("./shirt.png")
bag = Image.open("./bag.png")
sneaker = Image.open("./sneaker.png")

processed_shirt = ImageOps.fit(shirt, (28, 28))
processed_shirt = ImageOps.grayscale(processed_shirt)
processed_shirt = ImageOps.invert(processed_shirt)
processed_shirt.save("./processed_shirt.png")

processed_bag = ImageOps.fit(bag, (28, 28))
processed_bag = ImageOps.grayscale(processed_bag)
processed_bag = ImageOps.invert(processed_bag)
processed_bag.save("./processed_bag.png")

processed_sneaker = ImageOps.fit(sneaker, (28, 28))
processed_sneaker = ImageOps.grayscale(processed_sneaker)
processed_sneaker = ImageOps.invert(processed_sneaker)
processed_sneaker.save("./processed_sneaker.png")