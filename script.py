from tkinter import *
from PIL import Image, EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.56.1\bin\gswin64c.exe'

def save_as_png(canvas, fileName):
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

def generate_color_palette(color_encoding):
    result = []
    if color_encoding == "":
        for i in range(9):
            result.append("white")
        return result
    
    # for letter in color_encoding:


def create_diagram(canvas, width, height, width_buffer, height_buffer, color_encoding):
    triangle_height = height - height_buffer * 2
    triangle_base = width - width_buffer * 2
    outline_color = "black"
    color_palette = generate_color_palette(color_encoding)

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

root = Tk()

width = 500
height = 500
height_buffer = height/5
width_buffer = width/5
canvas = Canvas(root, width=width, height=height)

create_diagram(canvas=canvas, width=width, height=height, width_buffer=width_buffer, height_buffer=height_buffer, color_encoding="")
save_as_png(canvas, "testFile")

root.mainloop()