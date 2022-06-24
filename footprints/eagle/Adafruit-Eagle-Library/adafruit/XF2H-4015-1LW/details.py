###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "XF2H-4015-1LW")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/XF2H-4015-1LW")

newPart.addTag("description", """&lt;b&gt;Standard Rotary Backlock Type (0.5 mm-pitch)&lt;/b&gt;&lt;p&gt;
Source : http://www.omron.com/ecb/products/pdf/fpc.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-XF2H-4015-1LW",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='XF2H-4015-1LW')

OOMP.parts.append(newPart)