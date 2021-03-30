from ._anvil_designer import Station_sectionTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import Methods

class Station_section(Station_sectionTemplate):
  def __init__(self, rotate_angle_in = 0, train_id="109", train_occupation="R", track_type="disconnected track", station_type="interchange", station_name="Station_name", **properties):
    self.rotate_angle = rotate_angle_in
    self.train_id = train_id
    self.train_occupation = train_occupation
    self.track_type = track_type
    self.station_type = station_type
    self.station_name = station_name
    self.canvas_1.width="100"
    self.canvas_1.height="100"
    Methods.set_colours(self)
    self.init_components(**properties)
    
  def section_type(self):
    return "station"
  
  def display_station_empty_track(self):
     c = self.canvas_1
     if(self.rotate_angle == 45 or self.rotate_angle == 135 or self.rotate_angle == 225 or self.rotate_angle == 315):
        Methods.draw_line(self, c, 50, 45, 50, 54, 4, "black")
        Methods.draw_arc(self, c, 50, 37, 8, 0, 3.14*2, False, 2, "black")
        c.fill_style = Methods.set_station_colour(self, self.station_type)
        c.fill()
        c.font = "10px sans-serif"
        c.fill_text(self.station_name, 23, 20)
        
        img = self.canvas_1.get_image()
        self.image_1.source = anvil.image.rotate(img, 45)       
        self.canvas_1.reset_context()        
        self.canvas_1.draw_image(self.image_1.source, -20,-25 )
        
        Methods.draw_line(self, c, 0, 0, 100, 100, 4, "light_yellow")  
     else:
        Methods.draw_line(self, c, 50, 90, 50, 98, 4, "black")
        Methods.draw_arc(self, c, 50, 82, 8, 0, 3.14*2, False, 2, "black" )
        c.fill_style = Methods.set_station_colour(self, self.station_type)
        c.fill()
        c.font = "12px sans-serif"
        c.fill_text(self.station_name, 20, 65)
        
        Methods.draw_line(self, c, 0, 98, 100, 98, 4, "light_yellow")
      
     img = self.canvas_1.get_image()
     self.canvas_1.visible = False

     if(self.rotate_angle != 45 and self.rotate_angle != 225 and self.rotate_angle != 135 and self.rotate_angle != 315):
       self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
     elif (self.rotate_angle == 135 or self.rotate_angle == 315):
       self.image_1.source = anvil.image.rotate(img, self.rotate_angle-45)
     else:
       self.image_1.source = img
     
        
        
  def display_station_train_track(self, train_id, train_occupation):
    c = self.canvas_1
    
    if(self.rotate_angle == 45 or self.rotate_angle == 135 or self.rotate_angle == 225 or self.rotate_angle == 315):
        c.line_width = 3
        # Set the stroke and fill styles
        c.stroke_style, c.fill_style = Methods.set_train_colours(train_occupation)
        
        # Draw a filled rectangle  
        c.fill_rect(15, 30, 70, 16)
        c.stroke_rect(15, 30, 70, 16)
            
        c.fill_style, c.stroke_style = Methods.set_train_colours(train_occupation)
        c.fill_rect(55, 30, 30, 16)
        
        c.fill_style = self.white
        c.font = "15px sans-serif"
        c.fill_text(train_occupation, 60, 43)
        c.fill_text(train_id, 20, 43)
       
        Methods.draw_line(self, c, 50, 52, 50, 61, 4, "black")
        Methods.draw_arc(self, c, 50, 69, 8, 0, 3.14*2, False, 2, "black")
        c.fill_style = Methods.set_station_colour(self, self.station_type)
        c.fill()
        c.font = "10px sans-serif"
        c.fill_text(self.station_name, 20, 90)
        
        img = self.canvas_1.get_image()
        img_train = anvil.image.rotate(img, 45)
        self.canvas_1.visible = False
        self.canvas_1.reset_context()
        self.canvas_1.draw_image(img_train, -20,-20 )
        
        Methods.draw_line(self, c, 0, 0, 100, 100, 4, "light_yellow")
        
        img = self.canvas_1.get_image()
        c.visible=False
        if(self.rotate_angle == 45):
          self.image_1.source = img
        elif(self.rotate_angle == 225):
          self.image_1.source = anvil.image.rotate(img, 180)
        else:
          self.image_1.source = anvil.image.rotate(img, self.rotate_angle-45)
    else:
        Methods.draw_line(self, c, 0, 98, 100, 98, 4, "light_yellow")
        
        c.line_width = 3
        c.stroke_style, c.fill_style = Methods.set_train_colours(train_occupation)
 
        # Draw a filled rectangle  
        c.fill_rect(15, 78, 70, 16)
        c.stroke_rect(15, 78, 70, 16)
        
        c.fill_style, c.stroke_style = Methods.set_train_colours(train_occupation)
        c.fill_rect(55, 78, 30, 16)

        c.fill_style = self.white
        c.font = "15px sans-serif"
        c.fill_text(train_id, 20, 90)
        c.fill_text(train_occupation, 60, 90)
        
        Methods.draw_line(self, c, 9, 70, 9, 95, 4, "black")
        Methods.draw_arc(self, c, 9, 62, 8, 0, 3.14*2, False, 2, "black")
        
        c.fill_style = Methods.set_station_colour(self, self.station_type)
        
        c.fill()
        c.font = "12px sans-serif"
        c.fill_text(self.station_name, 20, 65)
  
        img = self.canvas_1.get_image()
        self.canvas_1.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
        
  def display_station_disconnected_track(self):
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
  
    if(self.rotate_angle == 45 or self.rotate_angle == 135 or self.rotate_angle == 225 or self.rotate_angle == 315):
      Methods.draw_line(self, c, 50, 40, 50, 49, 4, "black")
      Methods.draw_arc(self, c, 50, 32, 8, 0, 3.14*2, False, 2, "black")
      c.fill_style = Methods.set_station_colour(self, self.station_type)
      c.fill()
      
      c.font = "12px sans-serif"
      c.fill_text(self.station_name, 20, 20)
      
      img = self.canvas_1.get_image()
      
      self.canvas_1.visible = False
      c.reset_context()
      self.image_1.source = anvil.image.rotate(img, 225)

      c.draw_image(self.image_1.source, -20,-20)
      
      Methods.draw_line(self, c, 0, 0, 100, 100, 4, "dark_red")
      
      img = self.canvas_1.get_image()
      
      c.visible=False
      if(self.rotate_angle == 45):
        self.image_1.source = img
      elif(self.rotate_angle == 225):
        self.image_1.source = anvil.image.rotate(img, 180)
      else:
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle-45)
    else: 
      Methods.draw_line(self, c, 15, 50, 15, 96, 4, "black")
      Methods.draw_arc(self, c, 15, 42, 8, 0, 3.14*2, False, 2, "black")
      c.fill_style = Methods.set_station_colour(self, self.station_type)
      
      c.fill()
      c.font = "12px sans-serif"
      c.fill_text(self.station_name, 27, 45)
    
      Methods.draw_line(self, c, 0, 98, 100, 98, 4, "dark_red")
      
      img = self.canvas_1.get_image()
      self.canvas_1.visible = False
      self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      
  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    if(self.track_type == "empty track"):
      self.display_station_empty_track()
    elif(self.track_type == "train track"):
      self.display_station_train_track(self.train_id, self.train_occupation)
    elif(self.track_type == "disconnected track"):
      self.display_station_disconnected_track()
    else:
      print("The track type is wrong. It should be one of the following: \"empty track\", \"disconnected track\" or \"train track\"")
    
    


