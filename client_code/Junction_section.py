from ._anvil_designer import Junction_sectionTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import Methods
import anvil.server

class Junction_section(Junction_sectionTemplate):
  def __init__(self,rotate_angle=0, upside_down=True, curved = False, switch_position = True, track_type = "disconnected junction",  train_up = False, train_occupation = "F", train_id = "129", train_position_large_junction = "1", **properties):
    self.rotate_angle = rotate_angle
    self.curved = curved
    self.upside_down = upside_down
    self.switch_position = switch_position
    self.track_type = track_type
    self.train_up = train_up
    self.train_occupation = train_occupation
    self.train_id = train_id
    self.train_position_large_junction = train_position_large_junction
    if(track_type == "large junction" or track_type == "large train junction" or track_type == "disconnected large junction"):
      self.large_junction = True
    else:
      self.large_junction = False
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    Methods.set_colours(self)
    self.image_1.height = "120"
    self.canvas_1.width="120"
    self.canvas_1.height="120"

  def section_type(self):
    return "junction"
  
  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    if(self.track_type == "empty junction" or self.track_type == "large junction"):
      self.display_empty_junction()
    elif(self.track_type == "train junction" or self.track_type == "large train junction"):
      self.display_train_junction()
    elif(self.track_type == "disconnected junction" or self.track_type == "disconnected large junction"):
      self.display_disconnected_junction()
    else:
      print("The track type is wrong. It should be one of the following: \"empty junctio\", \"large junction\", \"train junction\", \"large train junction\", \"disconnected junction\" or \"disconnected large junction\"")


    
  def display_train_junction(self):
    c = self.canvas_1
    
    c.line_width = 3
    c.stroke_style, c.fill_style = Methods.set_train_colours(self.train_occupation)
    c.fill_rect(15, 78, 70, 16)
    c.stroke_rect(15, 78, 70, 16)
    c.fill_style, c.stroke_style = Methods.set_train_colours(self.train_occupation)
    c.fill_rect(55, 78, 30, 16)
    c.fill_style = self.white
    c.font = "15px sans-serif"
    c.fill_text(self.train_id, 20, 90)
    c.fill_text(self.train_occupation, 60, 90)
    
    img = c.get_image()
    c.reset_context()
    
    if(self.large_junction == False):
      if(self.upside_down == False):
        if(self.switch_position == False):
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 0, 98, 0, 3.14*2, False, 4, "very_light_gray")
            else:
              Methods.draw_line(self, c, 0, 100, 100, 0, 4, "very_light_gray")
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "light_yellow")
        else:
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "very_light_gray")
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 0, 98, 0, 3.14*2, False, 4, "light_yellow")
            else:
              Methods.draw_line(self, c, 0, 100, 100, 0, 4, "light_yellow")

        if(self.switch_position == False):
            if(self.train_up == True):
              c.draw_image(anvil.image.rotate(img, 90), 76, 0)
            else:
              c.draw_image(anvil.image.rotate(img, 270), 0, -10)
        else:
            if(self.curved == True):
              c.draw_image(anvil.image.rotate(img, 315), 15, -8, 120, 120)   
            else:
              if(self.train_up == True):
                c.draw_image(anvil.image.rotate(img, 315), -55, -68)
              else:
                c.draw_image(anvil.image.rotate(img, 135), -10, -8)
          
        img = self.canvas_1.get_image()
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      else:
        if(self.switch_position == False):
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 100, 98, 0, 3.14*2, False, 4, "very_light_gray")
            else:
              Methods.draw_line(self, c, 0, 0, 100, 100, 4, "very_light_gray")
            Methods.draw_line(self, c, 98, 0, 98, 120, 4, "light_yellow")
        else:
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "very_light_gray")
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 100, 98, 0, 3.14*2, False, 4, "light_yellow")
            else:
              Methods.draw_line(self, c, 0, 0, 100, 100, 4, "light_yellow")
       
        if(self.switch_position == False):
            if(self.train_up == True):
              c.draw_image(anvil.image.rotate(img, 90), 76, 0)
            else:
              c.draw_image(anvil.image.rotate(img, 270), 0, 0)
        else:
            if(self.curved == True):
              c.draw_image(anvil.image.rotate(img, 45), 42, -38, 120, 120)
            else:
              if(self.train_up == True):
                c.draw_image(anvil.image.rotate(img, 45), -5, -60)
              else:
                c.draw_image(anvil.image.rotate(img, 225), -74, -20)
        
        img = self.canvas_1.get_image()
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
    else:
      c.height = "200"
      c.width = "200"
      self.image_1.height = "200"
      c.reset_context()
      
      c.line_width = 3
      c.stroke_style, c.fill_style = Methods.set_train_colours(self.train_occupation)
      c.fill_rect(15, 78, 70, 16)
      c.stroke_rect(15, 78, 70, 16)
      c.fill_style, c.stroke_style = Methods.set_train_colours(self.train_occupation)
      c.fill_rect(55, 78, 30, 16)
      c.fill_style = self.white
      c.font = "15px sans-serif"
      c.fill_text(self.train_id, 20, 90)
      c.fill_text(self.train_occupation, 60, 90)
    
      img = c.get_image()
      c.reset_context()

      if(self.switch_position == False):
        Methods.draw_line(self, c, 102, 0, 102, 200, 4, "very_light_gray")
        Methods.draw_line(self, c, 0, 0, 200, 200, 4, "light_yellow")
        if(self.train_up == True):         
          c.draw_image(anvil.image.rotate(img, 45), -2, 0)
        elif (self.train_up == False):
          c.draw_image(anvil.image.rotate(img, 225), -65, -70)   
        img = c.get_image()
        c.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      else:
        Methods.draw_line(self, c, 0, 0, 200, 200, 4, "very_light_gray")
        Methods.draw_line(self, c, 102, 0, 102, 200, 4, "light_yellow")
        if(self.train_up == True):
          c.draw_image(anvil.image.rotate(img, 90), 0, 40)
        elif (self.train_up == False):
          c.draw_image(anvil.image.rotate(img, 270), 5, -40)
        img = c.get_image()
        c.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
           
  def display_empty_junction(self):  
    c = self.canvas_1
    if(self.large_junction == False):
      if(self.upside_down == False):
        if(self.switch_position == False):
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 0, 98, 0, 3.14*2, False, 4, "very_light_gray")
            else:
              Methods.draw_line(self, c, 0, 100, 100, 0, 4, "very_light_gray")
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "light_yellow")
        else:
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "very_light_gray")
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 0, 98, 0, 3.14*2, False, 4, "light_yellow")
            else:
              Methods.draw_line(self, c, 0, 100, 100, 0, 4, "light_yellow")
          
        img = self.canvas_1.get_image()
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      else:
        if(self.switch_position == False):
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 100, 98, 0, 3.14*2, False, 4, "very_light_gray")
            else:
              Methods.draw_line(self, c, 0, 0, 100, 100, 4, "very_light_gray")
            Methods.draw_line(self, c, 98, 0, 98, 120, 4, "light_yellow")
        else:
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "very_light_gray")
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 100, 98, 0, 3.14*2, False, 4, "light_yellow")
            else:
              Methods.draw_line(self, c, 0, 0, 100, 100, 4, "light_yellow")
              
        img = self.canvas_1.get_image()
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
    else:
      self.canvas_1.height = "200"
      self.canvas_1.width = "200"
      self.image_1.height = "200"
      self.canvas_1.reset_context()
      
      if(self.switch_position == False):
        Methods.draw_line(self, c, 102, 0, 102, 200, 4, "very_light_gray")
        Methods.draw_line(self, c, 0, 0, 200, 200, 4, "light_yellow")
        img = c.get_image()
        c.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      else:
        Methods.draw_line(self, c, 0, 0, 200, 200, 4, "very_light_gray")
        Methods.draw_line(self, c, 102, 0, 102, 200, 4, "light_yellow")
        img = c.get_image()
        c.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
  
  def display_disconnected_junction(self):
    c = self.canvas_1
    
    c.line_width = 3
    c.fill_style = self.red
    c.stroke_style = self.dark_red
    
    c.rotate(44.6)
    c.fill_rect(80, 10, 8, 40)
    c.stroke_rect(80, 10, 8, 40)
    
    c.rotate(36.4)
    c.fill_rect(-10, 68, 8, 41)
    c.stroke_rect(-10, 68, 8, 41)
 
    c.reset_transform()

    img = c.get_image()
    c.reset_context()

    if(self.large_junction == False):
      if(self.upside_down == False):
        if(self.switch_position == False):
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 0, 98, 0, 3.14*2, False, 4, "very_light_gray")
            else:
              Methods.draw_line(self, c, 0, 100, 100, 0, 4, "very_light_gray")
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "dark_red")
        else:
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "very_light_gray")
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 0, 98, 0, 3.14*2, False, 4, "dark_red")
            else:
              Methods.draw_line(self, c, 0, 100, 100, 0, 4, "dark_red")

        if(self.switch_position == False):
              c.draw_image(anvil.image.rotate(img, 90), 50, 0)
        else:
            if(self.curved == True):
              c.draw_image(anvil.image.rotate(img, 315), 18, 18, 100, 100)   
            else:
              c.draw_image(anvil.image.rotate(img, 315), -55, -50)

        img = self.canvas_1.get_image()
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      else:
        if(self.switch_position == False):
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 100, 98, 0, 3.14*2, False, 4, "very_light_gray")
            else:
              Methods.draw_line(self, c, 0, 0, 100, 100, 4, "very_light_gray")
            Methods.draw_line(self, c, 98, 0, 98, 120, 4, "dark_red")
        else:
            Methods.draw_line(self, c, 98, 0, 98, 100, 4, "very_light_gray")
            if(self.curved == True):
              Methods.draw_arc(self, c, 0, 100, 98, 0, 3.14*2, False, 4, "dark_red")
            else:
              Methods.draw_line(self, c, 0, 0, 100, 100, 4, "dark_red")
       
        if(self.switch_position == False):
              c.draw_image(anvil.image.rotate(img, 90), 50, 0)
        else:
            if(self.curved == True):
              c.draw_image(anvil.image.rotate(img, 45), 38, -30, 100, 100)
            else:  
              c.draw_image(anvil.image.rotate(img, 45), -10, -58)

        img = self.canvas_1.get_image()
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
    else:
      c.height = "200"
      c.width = "200"
      self.image_1.height = "200"
      c.reset_context()
      
      c.line_width = 3
      c.fill_style = self.red
      c.stroke_style = self.dark_red

      c.rotate(44.6)
      c.fill_rect(80, 10, 8, 40)
      c.stroke_rect(80, 10, 8, 40)

      c.rotate(36.4)
      c.fill_rect(-10, 68, 8, 41)
      c.stroke_rect(-10, 68, 8, 41)

      c.reset_transform()

      img = c.get_image()
      c.reset_context()
      
      if(self.switch_position == True):
        Methods.draw_line(self, c, 102, 0, 102, 200, 4, "very_light_gray")
        Methods.draw_line(self, c, 0, 0, 200, 200, 4, "dark_red")
        c.draw_image(anvil.image.rotate(img, 45), -10, 0)  
        img = c.get_image()
        c.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      else:
        Methods.draw_line(self, c, 0, 0, 200, 200, 4, "very_light_gray")
        Methods.draw_line(self, c, 102, 0, 102, 200, 4, "dark_red")
        c.draw_image(anvil.image.rotate(img, 90), 0, 50)
        img = c.get_image()
        c.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)

        
  


