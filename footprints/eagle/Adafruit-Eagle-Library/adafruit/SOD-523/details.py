###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "SOD-523")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/SOD-523")

newPart.addTag("description", """SOD-523 (0.8x1.2mm)

&lt;p&gt;Source: http://www.rohm.com/products/databook/di/pdf/rb751s-40.pdf&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-SOD-523",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='SOD-523')

OOMP.parts.append(newPart)