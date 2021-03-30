from ._anvil_designer import Track_sectionTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import Methods


class Track_section(Track_sectionTemplate):
  def __init__(self, rotate_angle_in = 0, train_id="097", train_occupation="R", track_type="disconnected track", l_shaped_curved=False, v_shaped_track = False, v_shaped_mirrored_track = False, v_shaped_train_position="2", **properties):
    self.rotate_angle = rotate_angle_in
    self.train_id = train_id
    self.train_occupation = train_occupation
    self.track_type = track_type
    self.l_shaped_curved = l_shaped_curved
    self.v_shaped_track = v_shaped_track
    self.v_shaped_mirrored_track = v_shaped_mirrored_track
    self.v_shaped_train_position = v_shaped_train_position
    self.canvas_1.width="100"
    self.canvas_1.height="100"
    self.init_components(**properties)
    Methods.set_colours(self)
    
  def section_type(self):
    return "track"
  
  def display_empty_track(self):
     c = self.canvas_1
     if(self.rotate_angle == 45 or self.rotate_angle == 135 or self.rotate_angle == 225 or self.rotate_angle == 315):
        Methods.draw_line(self, c, 0, 0, 100, 100, 4, "light_yellow")
     else:
        if(self.v_shaped_track == False and self.v_shaped_mirrored_track == False and self.l_shaped_curved == False):
          Methods.draw_line(self, c, 0, 98, 100, 98, 4, "light_yellow")
        elif(self.l_shaped_curved == True):
          Methods.draw_arc(self, c, 100, 0, 98, 0, 3.14*2, False, 4, "light_yellow")
        elif(self.v_shaped_track == True):
          Methods.draw_arc(self, c, 85, 100, 20, 0, 3.14*2, False, 4, "light_yellow")
          
          img = c.get_image()
          c.reset_context()
          c.draw_image(img, -63, -60)

          Methods.draw_line(self, c, 100, 100, 36, 25, 4, "light_yellow")
          Methods.draw_line(self, c, 2, 40, 2, 100, 4, "light_yellow")
        elif(self.v_shaped_mirrored_track == True):
          
          Methods.draw_arc(self, c, 10, 100, 20, 0, 3.14*2, False, 4, "light_yellow")
     
          img = c.get_image()
          c.reset_context()
          c.draw_image(img, 68, -60)

          c.stroke_style = self.light_yellow
          Methods.draw_line(self, c, 0, 100, 68, 22, 4, "light_yellow")
          Methods.draw_line(self, c, 98, 40, 98, 100, 4, "light_yellow")

        
     img = self.canvas_1.get_image()
     self.canvas_1.visible = False
     
     if(self.rotate_angle != 45 and self.rotate_angle != 225 and self.rotate_angle != 135 and self.rotate_angle != 315):
       self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
     elif (self.rotate_angle == 135 or self.rotate_angle == 315):
       self.image_1.source = anvil.image.rotate(img, self.rotate_angle-45)
     else:
       self.image_1.source = img
     
        
        
  def display_train_track(self, train_id, train_occupation):
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
      c.fill_text(train_id, 20, 43)
      c.fill_text(train_occupation, 60, 43)

      img = anvil.image.rotate(self.canvas_1.get_image(), 45)
      c.reset_context()
      self.canvas_1.visible = False           
      self.canvas_1.draw_image(img, -20,-20 )
      
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
      c.line_width = 3
      # Set the stroke and fill styles
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

      if(self.l_shaped_curved==True):
          img = c.get_image()
          c.reset_context()
          Methods.draw_arc(self, c, 100, 0, 98, 0, 3.14*2, False, 4, "light_yellow")
          c.draw_image(anvil.image.rotate(img, 45), -7, 8, 100, 100)
          
      elif(self.v_shaped_track == True):     
          img_train = c.get_image()
          c.reset_context()
          
          Methods.draw_arc(self, c, 85, 100, 20, 0, 3.14*2, False, 4, "light_yellow")

          img = c.get_image()
          c.reset_context()
          c.draw_image(img, -63, -60)

          Methods.draw_line(self, c, 100, 100, 36, 25, 4, "light_yellow")
          Methods.draw_line(self, c, 2, 40, 2, 100, 4, "light_yellow")
 
          if(self.v_shaped_train_position == "1"):
            c.draw_image(anvil.image.rotate(img_train, 50), 20, -10, 100, 100)
          elif(self.v_shaped_train_position == "2"):
            c.draw_image(anvil.image.rotate(img_train, 90), 0, 25, 80, 80)
            
      elif(self.v_shaped_mirrored_track == True):       
          img_train = c.get_image()
          c.reset_context()
          Methods.draw_arc(self, c, 10, 100, 20, 0, 3.14*2, False, 4, "light_yellow")
  
          img = c.get_image()
          c.reset_context()
          c.draw_image(img, 68, -60)
          
          Methods.draw_line(self, c, 0, 100, 68, 22, 4, "light_yellow")
          Methods.draw_line(self, c, 98, 40, 98, 100, 4, "light_yellow")
   
          if(self.v_shaped_train_position == "1"):
            c.draw_image(anvil.image.rotate(img_train, 130), 23, 20, 100, 100)
          elif(self.v_shaped_train_position == "2"):
            c.draw_image(anvil.image.rotate(img_train, 90), 78, 25, 80, 80)
      else:
          Methods.draw_line(self, c, 0, 98, 100, 98, 4, "light_yellow")
      img = self.canvas_1.get_image()
      self.canvas_1.visible = False
      self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      
      
  def display_disconnected_track(self):
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
      img = self.canvas_1.get_image()
      self.canvas_1.visible = False
      img_aux = anvil.image.rotate(img, 225)
      c.reset_context()
      c.draw_image(img_aux, -20,-20)
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
      if(self.l_shaped_curved == True):
        img = c.get_image()
        c.reset_context()       
        Methods.draw_arc(self, c, 100, 0, 98, 0, 3.14*2, False, 4, "dark_red")
       
        c.draw_image(anvil.image.rotate(img, 45), -25, 15, 100, 100)
        img = self.canvas_1.get_image()
        self.canvas_1.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      elif(self.v_shaped_track == True):
        img_X_sign = c.get_image()
        c.reset_context()
        
        Methods.draw_arc(self, c, 85, 100, 20, 0, 3.14*2, False, 4, "dark_red")

        img = c.get_image()

        c.reset_context()
        c.draw_image(img, -63, -60)
        
        Methods.draw_line(self, c, 100, 100, 36, 25, 4, "dark_red")
        Methods.draw_line(self, c, 2, 40, 2, 100, 4, "dark_red")
        
        c.draw_image(anvil.image.rotate(img_X_sign, 50), 45, -10, 100, 100)
        self.image_1.source = anvil.image.rotate(c.get_image(), self.rotate_angle)
      elif(self.v_shaped_mirrored_track == True):
        img_X_sign = c.get_image()
        c.reset_context()
        Methods.draw_arc(self, c, 10, 100, 20, 0, 3.14*2, False, 4, "dark_red")
        img = c.get_image()

        c.reset_context()
        c.draw_image(img, 68, -60)
        
        Methods.draw_line(self, c, 0, 100, 68, 22, 3.5, "dark_red")
        Methods.draw_line(self, c, 98, 40, 98, 100, 4, "dark_red")
        
        c.draw_image(anvil.image.rotate(img_X_sign, 130), -15, 10, 100, 100)
        self.image_1.source = anvil.image.rotate(c.get_image(), self.rotate_angle)
      else:        
        Methods.draw_line(self, c, 0, 98, 100, 98, 4, "dark_red")
        img = self.canvas_1.get_image()
        self.canvas_1.visible = False
        self.image_1.source = anvil.image.rotate(img, self.rotate_angle)
      
      
  def canvas_1_show(self, **event_args):  
    """This method is called when the Canvas is shown on the screen"""
    if(self.track_type == "empty track"):
      self.display_empty_track()
    elif(self.track_type == "train track"):
      self.display_train_track(self.train_id, self.train_occupation)
    elif(self.track_type == "disconnected track"):
      self.display_disconnected_track()
    else:
      print("The track type is wrong. It should be one of the following: \"empty track\", \"disconnected track\" or \"train track\"")
    
    

