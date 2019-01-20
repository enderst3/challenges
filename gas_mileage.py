"""
To introduce the problem think to my neighbor who drives a tanker truck. 
The level indicator is down and he is worried because he does not know if he will be able to make deliveries. 
We put the truck on a horizontal ground and measured the height of the liquid in the tank.

Fortunately the tank is a perfect cylinder and the vertical walls on each end are flat. 
The height of the remaining liquid is h, the diameter of the cylinder is d, 
the total volume is vt (h, d, vt are positive or null integers). You can assume that h <= d.

Could you calculate the remaining volume of the liquid? Your function tankvol(h, d, vt) 
returns an integer which is the truncated result (e.g floor) of your float calculation.

Examples:

tankvol(40,120,3500) should return 1021 (calculation gives about: 1021.26992027)

tankvol(60,120,3500) should return 1750

tankvol(80,120,3500) should return 2478 (calculation gives about: 2478.73007973)
"""

# see https://en.wikipedia.org/wiki/Circular_segment
# for the formulas used

from math import sin, acos, pi

def tankvol(h, d, vt):
    # radius
    r = d / 2.0
    # central angle of segment
    theta = 2 * acos(1 - h/r)
    # area of segment
    A_segment = r**2 / 2 * (theta - sin(theta))
    # area of circle
    A_circle = r**2 * pi
    # ratio of the areas
    ratio = A_segment / A_circle
    # remaining volume
    vol_remain = ratio * vt
    # return the truncated result
    return int(vol_remain)