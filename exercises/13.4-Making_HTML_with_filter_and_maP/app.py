all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color):
    return color["sexy"]

def generate_li(color):
    return "<li>{}</li>".format(color["label"])
	# return f'<li>{color["label"]}</li>'

sexy_colors = filter(filter_colors, all_colors)
sexy_color_lis = list(map(generate_li, sexy_colors))

print(sexy_color_lis)
