from PIL import Image,ImageChops
img1 = Image.open('image3.jpeg')
img2 = Image.open('image4.jpeg')
diff = ImageChops.difference(img1,img2)
if diff.getbbox():
   diff.show()