import json
import random as random
from tkinter import *
from PIL import Image, EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.56.1\bin\gswin64c.exe'

random.seed()
root = Tk()

width = 500
height = 500
height_buffer = height/5
width_buffer = width/5
canvas = Canvas(root, width=width, height=height)

# Colors are labelled by their starting letters
color_map = {
    "W": "white",
    "B": "blue",
    "R": "red",
    "G": "green",
    "P": "purple",
    "Y": "yellow",
    "O": "orange"
}
color_code_array = []
for key in color_map.keys():
    if key == "W":
        continue
    color_code_array.append(key)

# function to add to JSON
def write_json(new_data, filename):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["encodings"].update(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def save_as_png(canvas, fileName):
    # Opening JSON file
    f = open("./encoding_database.json")
    encoding_database = json.load(f)
    database_length = len(encoding_database["encodings"])
    # Writing to JSON file
    file_keyvalue = {str(database_length + 1) : fileName} 
    write_json(file_keyvalue, "./encoding_database.json")

    # save postscipt image 
    canvas.postscript(file = './eps/' + fileName + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open('./eps/' + fileName + '.eps') 
    img.save('./png/' + fileName + '.png', 'png')

def create_diagram_w_lines(canvas, width, height, width_buffer, height_buffer):
    # big triangle sides
    left_major = canvas.create_line(width/2, height_buffer,
                                    width_buffer, height - height_buffer)
    right_major = canvas.create_line(width/2, height_buffer,
                                    width - width_buffer, height - height_buffer)
    bottom_major = canvas.create_line(width_buffer, height - height_buffer,
                                    width - width_buffer, height - height_buffer)
    
    # horizontal cuts
    canvas.create_line(width_buffer + 1/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
                        width_buffer + 5/6 * triangle_base, height - height_buffer - 1/3 * triangle_height)
    canvas.create_line(width_buffer + 2/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
                        width_buffer + 4/6 * triangle_base, height - height_buffer - 2/3 * triangle_height)

    # bottom row slants
    canvas.create_line(width_buffer + 1/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
                        width_buffer + 2/6 * triangle_base, height - height_buffer - 0/3 * triangle_height)
    canvas.create_line(width_buffer + 2/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
                        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height)
    canvas.create_line(width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
                        width_buffer + 4/6 * triangle_base, height - height_buffer - 0/3 * triangle_height)
    canvas.create_line(width_buffer + 4/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
                        width_buffer + 5/6 * triangle_base, height - height_buffer - 1/3 * triangle_height)

    # middle row slants
    canvas.create_line(width_buffer + 2/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
                        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height)
    canvas.create_line(width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
                        width_buffer + 4/6 * triangle_base, height - height_buffer - 2/3 * triangle_height)

def process_color_encoding_string(color_encoding):
    result = ""
    for i in range(1, 10):
        num_index_in_code = color_encoding.find(str(i))
        if num_index_in_code == -1:
            result += str(i) + "W"
        else:
            result += color_encoding[num_index_in_code : num_index_in_code + 2]
    return result

def generate_color_palette(color_encoding):
    # Color Encoding String
    # Triangles are numbered 1 to 9 in order from top to bottom and left to right

    # The full color encoding string is 18 characters long, describing the color of each triangle
    # eg. 1R2W3W4W5W6P7B8Y9W stands for 1 red 2,3,4,5, white 6 purple 7 blue 8 yellow and 9 white
    # However, input strings will only be 6 characters long, describing the color of triangles
    # ONLY IF they are not WHITE
    # Thus, this method will process the input strings to convert them into
    color_encoding = process_color_encoding_string(color_encoding)
    print("Final fullstring encoding: " + color_encoding)

    result = []
    for i in range(9):
        result.append(color_map[color_encoding[i * 2 + 1 : i * 2 + 2]])
    return result

def create_diagram(canvas, width, height, width_buffer, height_buffer, color_encoding):
    triangle_height = height - height_buffer * 2
    triangle_base = width - width_buffer * 2
    outline_color = "black"
    color_palette = generate_color_palette(color_encoding)
    print("Color Palette: " + str(color_palette))

    # top row =============================================================================
    canvas.create_polygon([
        width_buffer + 3/6 * triangle_base, height - height_buffer - 3/3 * triangle_height,
        width_buffer + 2/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
        width_buffer + 4/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
    ],
    fill=color_palette[0],
    outline=outline_color,
    )

    # middle row =============================================================================
    canvas.create_polygon([
        width_buffer + 2/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
        width_buffer + 1/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
    ],
    fill=color_palette[1],
    outline=outline_color,
    )
    canvas.create_polygon([
        width_buffer + 2/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
        width_buffer + 4/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
    ],
    fill=color_palette[2],
    outline=outline_color,
    )
    canvas.create_polygon([
        width_buffer + 4/6 * triangle_base, height - height_buffer - 2/3 * triangle_height,
        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 5/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
    ],
    fill=color_palette[3],
    outline=outline_color,
    )

    # bottom row =============================================================================
    canvas.create_polygon([
        width_buffer + 1/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 0/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
        width_buffer + 2/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
    ],
    fill=color_palette[4],
    outline=outline_color,
    )
    canvas.create_polygon([
        width_buffer + 1/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 2/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
    ],
    fill=color_palette[5],
    outline=outline_color,
    )
    canvas.create_polygon([
        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 2/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
        width_buffer + 4/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
    ],
    fill=color_palette[6],
    outline=outline_color,
    )
    canvas.create_polygon([
        width_buffer + 3/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 5/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 4/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
    ],
    fill=color_palette[7],
    outline=outline_color,
    )
    canvas.create_polygon([
        width_buffer + 5/6 * triangle_base, height - height_buffer - 1/3 * triangle_height,
        width_buffer + 4/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
        width_buffer + 6/6 * triangle_base, height - height_buffer - 0/3 * triangle_height,
    ],
    fill=color_palette[8],
    outline=outline_color,
    )
    
    canvas.pack()
    canvas.update()

def generate_unique_code():
    code = ""
    num_set = {random.randint(1,9)}
    while len(num_set) < 3:
        num_set.add(random.randint(1,9))
    num_list = sorted(num_set)
    print("Num set: " + str(num_set))
    print("Num list: " + str(num_list))

    for i in range(6):
        if i % 2 == 0:
            code += str(num_list[int(i / 2)])
        else:
            arr_len = len(color_code_array)
            code += color_code_array[random.randint(0, arr_len - 1)]

    # TODO: Check if code exists alrdy!
    return code

def generate_diagrams(n):
    for i in range(n):
        color_encoding = generate_unique_code()
        print("Final generated color_encoding: " + color_encoding)
        create_diagram(canvas=canvas, width=width, height=height,
        width_buffer=width_buffer, height_buffer=height_buffer,
        color_encoding=color_encoding)
        save_as_png(canvas, color_encoding)

generate_diagrams(100)

root.mainloop()