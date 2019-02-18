from PIL import Image
import argparse
import os

# argparse moudle is 
parser = argparse.ArgumentParser()


parser.add_argument('file', type=str, 
					help='file name')
					
parser.add_argument('-o', action='store', 
					dest='output', type=str, 
					help='contrl output file')
					
parser.add_argument('--width', action='store', 
					dest='width', type=int, default=10, 
					help='the width of picture')
					
parser.add_argument('--height', action='store', 
					dest='height', type=int, default=10, 
					help='the height of picture')

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`.")

def get_char(r, g, b, alpha=256):
	if alpha == 0:
		return ' '
	
	lenght = len(ascii_char)
	
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	
	unit = (256.0 + 1) / lenght
	
	return ascii_char[int(gray / unit)]
	
if __name__ == '__main__':
	
	root_path = os.getcwd()
	picture_path = root_path + "/pictures/"
	output_path = root_path + "/output/"
	
	im = Image.open(picture_path + IMG)
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
	
	txt = ""
	
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j, i)))
		txt += '\r\n'
	print(txt)
	
	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open(output_path + "output3.txt", 'w') as f:
			f.write(txt)
