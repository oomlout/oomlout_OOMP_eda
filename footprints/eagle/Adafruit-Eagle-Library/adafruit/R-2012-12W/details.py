###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "R/2012-12W")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/R/2012-12W")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET R/EIA 2012-12 Wafe solder&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-R/2012-12W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='R/2012-12W')

OOMP.parts.append(newPart)