###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "A/3216-18R")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/A/3216-18R")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET A / EIA 3216-18 Reflow solder&lt;/b&gt;&lt;p&gt;
KEMET S / EIA 3216-12""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-A/3216-18R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='A/3216-18R')

OOMP.parts.append(newPart)