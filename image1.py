from PIL import Image, ImageFilter

img=Image.open('./images/meher1.jpg')


#filter_img=img.filter(ImageFilter.BLUR)
#box=(100, 50, 100, 50)
filter_img=img.convert('L')
#crooked=filter_img.rotate(90)
#resize=filter_img.resize((200,200))
box=(50,50, 100, 100)
region=filter_img.crop(box)

region.save('grey.png', 'png')
region.show()


# print(img)
#
# print(img.format)
#print(img.size)
#print(resize.size)
# print(img.mode)
# #print(dir(img))
#
# print('Meher')