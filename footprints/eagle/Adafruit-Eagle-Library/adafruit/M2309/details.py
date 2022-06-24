###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "M2309")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/M2309")

newPart.addTag("description", """&lt;b&gt;RESISTOR&lt;/b&gt;&lt;p&gt;
MELF 0.25 W""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-M2309",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='M2309')

OOMP.parts.append(newPart)