from PIL import Image

# RGB values for recoloring.
navy = (0, 0, 128)
plum = (221, 160, 221)
aquamarine = (127, 255, 212)
yellow = (252, 227, 166)

# Import image
# change IMAGENAME to the path on your computer to the image 
# you're using'''

my_image = Image.open("lina2.jpeg") 

# each pixel is represented in the form 
# (red value, green value, blue value, transparency)
image_list = my_image.getdata()  

# Turns the sequence above into a list, it can be iterated through
# in a loop
#image_list = list(image_list)
print(len(image_list))

for x in image_list:
	intensity=x[0]+x[1]+x[2]




# list that will hold the pixel data for the new image
recolored = [] 
#**************************************************#
#**************************************************#

#YOUR CODE to loop through the original list of pixels and 
# build a new list based on intensity should go here.
for x in image_list:
	intensity=x[0]+x[1]+x[2]
	
	if intensity <182:
		recolored.append(navy)

	elif intensity>=182 and intensity<364:
		recolored.append(plum)

	elif intensity>=364 and intensity<546:
		recolored.append(aquamarine)

	else:
		recolored.append(yellow)
#**************************************************#
#**************************************************#
# Create a new image using the recolored list. Display and save 
# the image.

# Creates a new image that will be the same size as the original
new_image = Image.new("RGB", my_image.size)

# Adds the data from the recolored list to the image
new_image.putdata(recolored)

# Opens the new image on the screen
new_image.show() 

# Saves the new image as "recolored.jpg"
new_image.save("recolored.jpg", "jpeg") 
