from ._anvil_designer import Main_pageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Junction_section import Junction_section
from ..Track_section import Track_section

import time
import anvil.server

class Main_page(Main_pageTemplate):
  
  def __init__(self, **properties):   
    # Set Form properties and Data Bindings.
    
    #Just for testing
    first_train = app_tables.trains.get(Name = "1233")
    first_train.update(Location=app_tables.location.get(Location = "junction_8"), Direction=True)
    
    second_train = app_tables.trains.get(Name = "1B98")
    second_train.update(Location=app_tables.location.get(Location = "junction_4"), Direction=False)
    
    self.old_tracks_table = app_tables.location.search()
    self.current_tracks_table = app_tables.location.search()
    
    self.old_trains_table = app_tables.trains.search()
    self.current_trains_table = app_tables.trains.search()
   
    self.tiles ={
    "track_section_34": self.track_section_34,
    "track_section_1": self.track_section_1,
    "track_section_2": self.track_section_2,
    "track_section_3": self.track_section_3,
    "track_section_4": self.track_section_4,
    "track_section_49": self.track_section_49,
    "track_section_6": self.track_section_6,
    "station_section_1": self.station_section_1,
    "track_section_35":  self.track_section_35,
    "junction_4": self.junction_4,
    "junction_1": self.junction_1,
    "track_section_5": self.track_section_5,
    "track_section_36": self.track_section_36,
    "station_section_4": self.station_section_4,
    "track_section_42": self.track_section_42,
    "track_section_22": self.track_section_22,
    "track_section_20": self.track_section_20,
    "junction_2": self.junction_2,
    "track_section_27": self.track_section_37,
    "junction_5": self.junction_5,
    "track_section_13": self.track_section_13,
    "track_section_23": self.track_section_23,
    "track_section_19": self.track_section_19,
    "track_section_50": self.track_section_50,
    "track_section_38": self.track_section_38,
    "track_section_14": self.track_section_14,
    "station_section_3": self.station_section_3,
    "track_section_18": self.track_section_18,
    "track_section_7": self.track_section_7,
    "track_section_39": self.track_section_39,
    "station_section_5": self.station_section_5,
    "junction_9": self.junction_9,
    "track_section_46": self.track_section_46,
    "station_section_2": self.station_section_2,
    "station_section_8": self.station_section_8,
    "track_section_15": self.track_section_15,
    "track_section_17": self.track_section_17,
    "track_section_8": self.track_section_8,
    "track_section_40": self.track_section_40,
    "junction_6": self.junction_6,
    "track_section_16": self.track_section_16,
    "track_section_25": self.track_section_25,
    "track_section_10": self.track_section_10,
    "track_section_12": self.track_section_12,
    "track_section_48": self.track_section_48,
    "track_section_21": self.track_section_21,
    "track_section_43": self.track_section_43,
    "station_section_6": self.station_section_6,
    "track_section_9": self.track_section_9,
    "junction_3": self.junction_3,
    "track_section_41": self.track_section_41,
    "junction_8": self.junction_8,
    "track_section_33": self.track_section_33,
    "track_section_32": self.track_section_32,
    "track_section_31": self.track_section_31,
    "track_section_30": self.track_section_30,
    "track_section_29": self.track_section_29,
    "track_section_51": self.track_section_51,
    "track_section_28": self.track_section_28,
    "junction_7": self.junction_7,
    "station_section_7": self.station_section_7,
    "track_section_27": self.track_section_27,
    "track_section_24": self.track_section_24,
      
    }
    
    for row in app_tables.trains.search():
      self.new_row = row
      self.update_train_track()
    
# ----------------------- EXTRA --------------------------
#     self.junctions_position = {
#       "junction_1": [800, 96],
#       "junction_2": [1100, 200],
#       "junction_3": [1100, 800],
#       "junction_4": [95, 97],
#       "junction_5": [300, 300],
#       "junction_6": [300, 700],
#       "junction_7": [900, 900],
#       "junction_8": [100, 900],
#       "track_section_42": [400, 200],
#       "track_section_43": [400, 800]
#     }

    self.init_components(**properties)
    
    
  def update_train_track(self):
    current_tile = self.tiles.get(self.new_row['Location']['Location']) 
    # update the train's position accordingly
    # firstly, set the train's id
    current_tile.train_id = self.new_row['Name']
    # then set the train's occupation according to the type
    current_tile.train_occupation = self.new_row['Type']
    
    if(self.new_row['Location']['Location'] == "junction_9"): 
        current_tile.train_position_large_junction = "2"
        current_tile.track_type = "large train junction"
        current_tile.switch_position = self.new_row['Direction']
        current_tile.canvas_1.reset_context()
        current_tile.canvas_1_show()
    # if the current location is a junction
    elif(current_tile.section_type() == "junction"):
        current_tile.track_type = "train junction"
        # set the right position of the train which depends on the current direction
        current_tile.switch_position = self.new_row['Direction']
        current_tile.canvas_1.reset_context()
        current_tile.canvas_1_show()
    else:
        current_tile.track_type = "train track"
        # reset the context and display the train
        current_tile.canvas_1.reset_context()
        current_tile.canvas_1_show()
                 
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    with anvil.server.no_loading_indicator:
      if(self.is_train_database_updated() is True):
          self.new_row, self.old_row = self.get_train_rows()
          tile = self.tiles.get(self.old_row['Location']['Location'])

          if(tile.section_type() == "junction"):
            tile.track_type = "empty junction"
          else:
            tile.track_type = "empty track"
           
          tile.canvas_1.reset_context()
          tile.canvas_1_show()
            
          self.update_train_track()
          
      if(self.is_tracks_database_updated() is True):
        self.old_tracks_table = self.current_tracks_table
        self.current_tracks_table = app_tables.location.search()
        for row_1, row_2 in zip(self.current_tracks_table, self.old_tracks_table):
          if(row_1['Track_status'] != row_2['Track_status']):
              row = row_1
              break
        self.update_disconnected_track(row)
          
  def is_train_database_updated(self):
    trains_table = app_tables.trains.search()
    for row_1, row_2 in zip(self.current_trains_table, trains_table):
      if(row_1['Location'] != row_2['Location'] or row_1['Direction'] != row_2['Direction']):
        return True
    return False
    
  def get_train_rows(self):
    self.old_trains_table = self.current_trains_table
    self.current_trains_table = app_tables.trains.search()
    for row_1, row_2 in zip(self.current_trains_table, self.old_trains_table):
      if(row_1['Location'] != row_2['Location'] or row_1['Direction'] != row_2['Direction']):
        return row_1, row_2
      
  def is_tracks_database_updated(self):
    tracks_table = app_tables.location.search()
    for row_1, row_2 in zip(self.current_tracks_table, tracks_table):
      if(row_1['Track_status'] != row_2['Track_status'] or row_1['Direction'] != row_2['Direction']):
        return True
    return False
  
  def update_disconnected_track(self, row):
    tile = self.tiles.get(row['Location'])
    is_connected = row['Track_status']
    direction = row['Direction']
    if(is_connected is False):
      if(tile.section_type() == "track" or tile.section_type() == "station"):
        tile.track_type = "disconnected track"
      elif(row['Location'] == "junction_9"):
        tile.track_type = "disconnected large junction"
        tile.switch_position = direction
      elif(tile.section_type() == "junction"):
        tile.track_type = "disconnected junction"
        tile.switch_position = direction
    else:
        if(tile.section_type() == "track" or tile.section_type() == "station"):
          tile.track_type = "empty track"
        elif(row['Location'] == "junction_9"):
          tile.track_type = "large junction"
          tile.switch_position = direction
        elif(tile.section_type() == "junction"):
          tile.track_type = "empty junction"
          tile.switch_position = direction
    
    tile.canvas_1.reset_context()
    tile.canvas_1_show()
  
#   def get_new_l_shaped_track(self, track):
#       rotate_angle = track.rotate_angle
#       train_id = track.train_id
#       train_occupation = track.train_occupation
#       track_type = "train track"
#       l_shaped_curved = track.l_shaped_curved
#       v_shaped_track = track.v_shaped_track
#       v_shaped_mirrored_track = track.v_shaped_mirrored_track
#       v_shaped_train_position = track.v_shaped_train_position
#       return Track_section(rotate_angle, train_id, train_occupation, track_type, l_shaped_curved, v_shaped_track, v_shaped_mirrored_track, v_shaped_train_position)
        
#   def display_l_shaped_section(self, current_tile):
#         current_tile.track_type = "train track"
#         previous_tile_name = self.old_row['Location']['Location']
        
#         if(self.new_row['Location']['Location'] == "track_section_42"):
#           if(previous_tile_name == "junction_5"):
#             self.display_l_shaped_section_different_width(current_tile)          
# # ------------------------------------ EXTRA --------------------------------------------
# #             time.sleep(0.5)
# #             new_l_shaped_track = self.get_new_l_shaped_track(current_tile)
# #             current_tile.remove_from_parent()

# #             x_in = self.junctions_position.get(self.new_row['Location']['Location'])[0]
# #             y_in = self.junctions_position.get(self.new_row['Location']['Location'])[1]
# #             width_in = 100
# #             current_tile = new_l_shaped_track
# #             current_tile.v_shaped_train_position = "1"
# #             self.xy_panel_1.add_component(current_tile, x=x_in, y=y_in, width=width_in)

# #             self.tiles[key] = current_tile
#           else:
#             self.display_l_shaped_section_same_width(current_tile)
      
# # ------------------------------------ EXTRA --------------------------------------------
# #             time.sleep(0.5)
# #             current_tile.v_shaped_train_position = "2"
# #             new_l_shaped_track = self.get_new_l_shaped_track(current_tile)
# #             current_tile.remove_from_parent()

# #             current_tile = new_l_shaped_track
# #             x_in = self.junctions_position.get(self.new_row['Location']['Location'])[0]
# #             y_in = self.junctions_position.get(self.new_row['Location']['Location'])[1]
# #             width_in = 120

# #             self.xy_panel_1.add_component(new_l_shaped_track, x=x_in-20, y=y_in, width=width_in)

# #             key = self.location[current_row_nr]

# #             self.tiles[key] = current_tile
#         elif(self.location[current_row_nr] == "track_section_43"):
#           if(self.old_locations[self.position] == "junction_6"):
#             self.display_l_shaped_section_different_width(current_tile)
            
# # ------------------------------------ EXTRA --------------------------------------------
# #             time.sleep(0.5)
# #             new_l_shaped_track = self.get_new_l_shaped_track(current_tile)
# #             current_tile.remove_from_parent()

# #             x_in = self.junctions_position.get(self.new_row['Location']['Location'])[0]
# #             y_in = self.junctions_position.get(self.new_row['Location']['Location'])[1]
# #             width_in = 100
# #             current_tile = new_l_shaped_track
# #             current_tile.v_shaped_train_position = "1"
# #             self.xy_panel_1.add_component(current_tile, x=x_in, y=y_in, width=width_in)


# #             self.tiles[key] = current_tile
#           else:
#             self.display_l_shaped_section_same_width(current_tile)
          
# # ------------------------------------ EXTRA --------------------------------------------
# #             time.sleep(0.5)
# #             current_tile.v_shaped_train_position = "2"
# #             new_l_shaped_track = self.get_new_l_shaped_track(current_tile)
# #             current_tile.remove_from_parent()

# #             current_tile = new_l_shaped_track
# #             x_in = self.junctions_position.get(self.new_row['Location']['Location'])[0]
# #             y_in = self.junctions_position.get(self.new_row['Location']['Location'])[1]
# #             width_in = 120

# #             self.xy_panel_1.add_component(new_l_shaped_track, x=x_in-20, y=y_in, width=width_in)

# #             key = self.new_row['Location']['Location']

# #             self.tiles[key] = current_tile
  
#   def display_l_shaped_section_different_width(self, tile):
#     tile.v_shaped_train_position = "2"
#     new_l_shaped_track = self.get_new_l_shaped_track(tile)
#     tile.remove_from_parent()

#     x_in = self.junctions_position.get(self.new_row['Location']['Location'])[0]
#     y_in = self.junctions_position.get(self.new_row['Location']['Location'])[1]
#     width_in = 120

#     self.xy_panel_1.add_component(new_l_shaped_track, x=x_in-20, y=y_in, width=width_in)

#     key = self.new_row['Location']['Location']
#     self.tiles[key] = new_l_shaped_track
                                
#   def display_l_shaped_section_same_width(self, tile):
#     tile.v_shaped_train_position = "1"
#     tile.canvas_1.reset_context()
#     tile.canvas_1_show()       
           


    
   