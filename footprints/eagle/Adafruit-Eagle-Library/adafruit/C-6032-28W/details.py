###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "C/6032-28W")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/C/6032-28W")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET C / EIA 6032-28 Wafe solder&lt;/b&gt;&lt;p&gt;
KEMET U / EIA 6032-15""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-C/6032-28W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='C/6032-28W')

OOMP.parts.append(newPart)