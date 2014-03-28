This post provides a listing of the Raspberry Pi prototype code that produced the image shown in My-Fourth-Post and 
the image below.  All code, 3-D model, and other associated files can be found in the project_code directory.


#!/usr/bin/python
# Earth_Skull.py
from __future__ import absolute_import, division, print_function, unicode_literals
""" 
Simple textruring of Sphere objects against a plane. The atmosphere has
blend set to True and so has to be drawn after object behind it to allow them
to show through.  Uses the import pi3d method to load *everything*
"""
from math import sin, cos
import demo
import pi3d
# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(x=50, y=50)
DISPLAY.set_background(0,0,0,1)    	# r,g,b,alpha
shader = pi3d.Shader("uv_reflect")
flatsh = pi3d.Shader("uv_flat")
skull_shader = pi3d.Shader("mat_light")
#========================================
# Setting 2nd param to True renders 'True' Blending
# (this can be changed later to 'False' with 'cloudimg.blend = False')
clouds_image = pi3d.Texture("textures/earth_clouds.png",True)
earth_image = pi3d.Texture("textures/world_map.jpg",True)
stars_image = pi3d.Texture("textures/stars2.jpg")
water_image = pi3d.Texture("textures/water.jpg")
# Load shapes
earth_sphere = pi3d.Sphere(radius=2, slices=24, sides=24,
                  name="earth", z=5.8)
                  
earth_sphere.set_alpha(0.5)
atmo_sphere = pi3d.Sphere(radius=2.05, slices=24, sides=24,
                   name="clouds", z=5.8)
star_plane = pi3d.Plane(w=50, h=50, name="stars", z=20)

skull_model = pi3d.Model(file_string='models/skull_1.obj', name='skull_1', 
              y=-1.8, z=6.0, sx=0.5, sy=0.5, sz=0.5)
skull_model.set_shader(skull_shader)

# Fetch key presses
the_keys = pi3d.Keyboard()

# Display scene
while DISPLAY.loop_running():
  earth_sphere.rotateIncY(-0.1)
  atmo_sphere.rotateIncY(-0.14)
  skull_model.rotateIncY(-0.1)

  skull_model.draw()
  earth_sphere.draw(shader, [earth_image])
  star_plane.draw(flatsh,[stars_image])
  atmo_sphere.draw(shader, [clouds_image]) # this has to be last as blend = True

  k = the_keys.read()
  if k >-1:
    # p key pressed
    if k==112:
      pi3d.screenshot("earth_skull.jpg")
    # escape key pressed
    elif k==27:
      the_keys.close()
      DISPLAY.stop()
      break


![Prototype Snapshot](../project_images/Earth_Skull.jpg?raw=true "Prototype Snapshot")
