from PIL import Image
import numpy as np
import os
#~ import join
import time

def image(original_picture_dir, transformed_picture_dir, depths=10):
	# Open a image and transfered to array
	img_array = np.asarray(Image.open(original_picture_dir).convert('L')).astype('float')
	# Range of depth is [0-100], default is 10
	depth = depths
	# Get the gradient of image
	grad = np.gradient(img_array)
	# Get the horizon and vetical axis gradient of image
	grad_x, grad_y = grad
	# Normlization of horizon and vertical axis respectively
	grad_x = grad_x * depth / 100.
	grad_y = grad_y * depth / 100.
	
	A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
	
	uni_x = grad_x / A
	uni_y = grad_y / A
	uni_z = 1. / A
	# Elivation angle from light source, randia
	vec_el = np.pi / 2.2
	# Azimuth angle from light source, randia
	vec_az = np.pi / 4.
	
	# Effection that light source to axis x, y and z, respectively.
	dx = np.cos(vec_el) * np.cos(vec_az)
	dy = np.cos(vec_el) * np.sin(vec_az)
	dz = np.sin(vec_el)
	
	# Normlization of light source
	b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
	b = b.clip(0, 255)
	
	# Re-construction image
	im = Image.fromarray(b.astype('uint8'))
	# Save transformed image
	im.save(transformed_picture_dir)
	
def main():
	depth = 10
	start_time = time.clock()
	
	root_path = os.getcwd() + '/'
	pictures_list = os.listdir(root_path + 'data')
	
	time.sleep(2)
	
	for starts in pictures_list:
		start = ''.join(starts)
		original_picture_dir = root_path  + 'data/' + start
		transformed_picture_dir = root_path + 'data/' + 'HD_' + start
		
		image(original_picture_dir=original_picture_dir, 
				transformed_picture_dir=transformed_picture_dir, depths=depth)
		
	end_time = time.clock()
	print('Total running time :' + str(end_time - start_time) +' seconds')
	time.sleep(2)
	
if __name__ == '__main__':
	main()
