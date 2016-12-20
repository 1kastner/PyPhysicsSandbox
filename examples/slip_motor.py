"""
An example of using slip motors on shapes.  The screencast developing this code can be found
here:
"""

from pyphysicssandbox import *

window('Slip Motors', 300, 300)
gravity(0, 0)

arm1 = box((100, 100), 100, 10, 100)
arm1.color = Color("yellow")

pivot1 = pivot((105, 105))
pivot1.connect(arm1)

# Play with the stiffness and damping values to get
# different behaviors of the spring attached to the motor
slip_motor(arm1, pivot1, 45, 20000000, 900000, -45, 3).debug = True
arm1.debug = True

run()
