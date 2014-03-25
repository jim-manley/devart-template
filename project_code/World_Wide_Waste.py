#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
"""
World_Wide_Waste.py prototype initial version 0.000001
Based on the Pi3D Earth.py demo found at 
https://github.com/pi3d/pi3d_demos/blob/master/Earth.py
The atmosphere has blend set to True, and so has to be drawn after the object behind 
it to allow it to show through.  Use the import pi3d method to load *everything*
"""
from math import sin, cos
import demo
import pi3d
# Setup display and initialize pi3d
DISPLAY = pi3d.Display.create(x=50, y=50)
DISPLAY.set_background(0,0,0,1)    	# r,g,b,alpha
shader = pi3d.Shader("uv_reflect")
flatsh = pi3d.Shader("uv_flat")
#========================================
# Setting 2nd param to True renders 'True' blending
# (this can be changed later to 'False' with 'cloud_image.blend = False')
cloud_image = pi3d.Texture("textures/clouds_map.png",True)
earth_image = pi3d.Texture("textures/earth_map.jpg")
stars_image = pi3d.Texture("textures/stars.jpg")
water_image = pi3d.Texture("textures/water.jpg")
# Load shapes
earth_sphere = pi3d.Sphere(radius=2, slices=24, sides=24,
                  name="earth", z=5.8)
clouds_sphere = pi3d.Sphere(radius=2.05, slices=24, sides=24,
                   name="clouds", z=5.8)
stars_plane = pi3d.Plane(w=50, h=50, name="stars", z=30)
# Fetch key presses
the_keys = pi3d.Keyboard()

# Display scene
while DISPLAY.loop_running():
  stars_plane.rotateIncZ(0.01)
  earth_sphere.rotateIncY(-0.1)
  clouds_sphere.rotateIncY(-0.14)

  earth_sphere.draw(shader, [earth_image])
  stars_plane.draw(flatsh,[stars_image])
  clouds_sphere.draw(shader, [clouds_image]) # this has to be last as blend = True

  k = they_keys.read()
  if k >-1:
    # p key is pressed
    if k==112:
      pi3d.screenshot("earth.jpg")
    # escape key is pressed
    elif k==27:
      the_keys.close()
      DISPLAY.stop()
      break
