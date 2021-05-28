import random

def generate_colors(n, mode):
	colors = []
	i = 0
	if n <= 5:
		while i < n:
			colors_tmp = []
			x = 0
			while x < 4:
				if mode == "light":
					colors_tmp.append(generate_color1())
				elif mode == "dark":
					colors_tmp.append(generate_color1())
				x += 1
			colors.append(colors_tmp)
			i += 1
	else:
		while i < n:
			colors_tmp = []
			x = 0
			while x < 4:
				if mode == "light":
					#tu generuj kolor
					colors_tmp.append(generate_color2())
				elif mode == "dark":
					#tu generuj kolor inny
					colors_tmp.append(generate_color2())
				x += 1
			colors.append(colors_tmp)
			i += 1
	return colors

def generate_color1():
	r = 77
	g = 224
	b = 204
	a = random.uniform(0.45, 0.71)
	rgba_template = [r, g, b, a]
	name = 'rgba(' + ((str(rgba_template)).replace("[","")).replace("]","") +')'
	return name


def generate_color2():
	r = random.randint(104, 213)
	g = random.randint(149, 237)
	b = random.randint(104, 237)
	a = 0.61
	rgba_template = [r, g, b, a]
	name = 'rgba(' + ((str(rgba_template)).replace("[","")).replace("]","") +')'
	return name
print (generate_colors(4,"light"))