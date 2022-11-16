from PIL import Image

# def resize_image(sizel, size2) :
image = Image.open('nature.jfif')

print(f"Current size : {image.size}" )

resized_image = image.resize(( 500, 500 ))             
resized_image.save('nature1.jfif') 


""" resized_image = image.resize(( sizel, size2))
    
    resized_image.save(' nature' + str(size1) + '.jfif')

size1 = int(input('Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1, size2) """