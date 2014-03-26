# World Wide Waste
- Life is Temporary on a Fragile Blue Planet

## Author
- Jim Manley
- GitHub Account: jim-manley

## Description
World Wide Waste provides the visitor an interactive glimpse of how sensitive our planet's resources are to our actions.  A 3-D spherical model of the Earth rotates, using NASA visible imagery of terrain and ocean surfaces as a texture map.  The atmosphere is represented in a slightly larger separate spherical model with a transparent-background texture map derived from NASA infrared satellite imagery that shows cloud cover world-wide, and it is rotating at a slightly different rate from the planet model.

Interactivity is implemented via either camera-tracked hand gestures or button/trackball input so that visitors can change the longitudinal orientation and tilt of the Earth's axis to view the weather at any location on the planet while it continues rotating.  They can also blow on the display and cause the cloud layer and terrain to scatter, representing human devastation that can be caused all-too-easily by every inhabitant at any moment. 

## Link to Prototype

Currently, the output of the software is a 6 gigabit/second 1080p/60Hz signal coming directly out of the Raspberry Pi's HDMI port.  A reduced-resolution stream that can be viewed via a browser will be provided in a future update.

[On-line Prototype Demo Placeholder Link](http://www.google.com "On-line Prototype Demo Placeholder Link")

## Example Code
```
#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
"""
Based on Earth.py demo at https://github.com/pi3d/pi3d_demos/blob/master/Earth.py
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
```
## Links to External Libraries

[Pi3D Python Library](https://github.com/tipam/pi3d "Pi3D Python Library")

## Images & Videos

![Earth Terrain Texture Map](https://github.com/pi3d/pi3d_demos/blob/master/textures/world_map.jpg?raw=true "Earth Terrain Texture Map")

![Clouds Texture Map](http://raspberry_office.byethost11.com/Planets/Earth_Clouds_on_Black.jpg?raw=true "Clouds Texture Map")

![Project Snapshot](http://raspberry_office.byethost11.com/Planets/Earth.jpg?raw=true "Project Snapshot")
