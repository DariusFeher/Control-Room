import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def set_colours(component):
  component.light_yellow = "#FFD54F"
  component.white = "#FFFFFF"
  component.dark_red = "#DD2C00"
  component.red = "#FF3D00"
  component.dark_blue = "#0277BD"
  component.blue = "#40C4FF"
  component.light_red = "#F44336"
  component.pink = "#FF8A80"
  component.dark_gray = "#757575"
  component.light_gray = "#BDBDBD"
  component.black = "#000000"
  component.cyan = "#009688"
  component.very_light_gray = "#EEEEEE"
  
def set_train_colours(train_occupation):
  dark_blue = "#0277BD"
  blue = "#40C4FF"
  light_red = "#F44336"
  pink = "#FF8A80"
  dark_gray = "#757575"
  light_gray = "#BDBDBD"
  
  if(train_occupation == "R"):
      stroke_style = dark_blue
      fill_style = blue
  elif(train_occupation == "HS"):
      stroke_style = light_red
      fill_style = pink
  else:
      stroke_style = dark_gray
      fill_style = light_gray
      
  return stroke_style, fill_style

def set_station_colour(component, station_type):
    if(station_type == "regional"):
      fill_style = component.dark_blue
    elif (station_type == "main"):
      fill_style = component.light_red
    elif(station_type == "interchange"):
      fill_style = component.cyan
    return fill_style

def get_stroke_style_colour(component, stroke_style):
  if(stroke_style == "light_yellow"):
    return component.light_yellow
  elif(stroke_style == "white"):
    return component.white
  elif(stroke_style == "dark_red"):
    return component.dark_red
  elif(stroke_style == "red"):
    return component.red
  elif(stroke_style == "dark_blue"):
    return component.dark_blue
  elif(stroke_style == "blue"):
    return component.blue
  elif(stroke_style == "light_red"):
    return component.light_red
  elif(stroke_style == "pink"):
    return component.pink
  elif(stroke_style == "dark_gray"):
    return component.dark_gray
  elif(stroke_style == "light_gray"):
    return component.light_gray
  elif(stroke_style == "black"):
    return component.black
  elif(stroke_style == "very_light_gray"):
    return component.very_light_gray
  
  
def draw_arc(component, canvas, x, y, radius, start_angle, end_angle, anticlockwise, line_width, stroke_style):
    canvas.stroke_style = get_stroke_style_colour(component, stroke_style)
    canvas.begin_path()
    canvas.arc(x, y, radius, start_angle, end_angle, anticlockwise)
    canvas.close_path()
    canvas.line_width = line_width
    canvas.stroke()
    
    
def draw_line(component, canvas, x1, y1, x2, y2, line_width, stroke_style):
  canvas.stroke_style = get_stroke_style_colour(component, stroke_style)
  canvas.begin_path()
  canvas.move_to(x1, y1)
  canvas.line_to(x1, y1)
  canvas.line_to(x2, y2)
  canvas.close_path()
  canvas.line_width = line_width
  canvas.stroke()

