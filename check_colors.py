#import Pillow 
#from colors.py import generate_colors
import colorthief
from colorthief import ColorThief
import glob
from pathlib import Path

def get_colors(image):
	dominant_color = ColorThief(image).get_color(quality=1)
	return dominant_color

#print (get_colors('blockchains/polygon/info/logo.png'))

def get_files():
	files = list(Path('blockchains').glob('**/*.png'))
	return files

#print (get_files())

def main():
	colors_list = []

	for i in get_files():
		color = get_colors(i)
		name = str(i).split('/')[-2]
		if name == 'info':
			name = str(i).split('/')[-3]
		tmp = {name: color}	
		colors_list.append(tmp)
	print(colors_list)	


main()

		


       