###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "B/3528-21W")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/B/3528-21W")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET B / EIA 3528-21 Wave solder&lt;/b&gt;&lt;p&gt;
KEMET T / EIA 3528-12""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-B/3528-21W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='B/3528-21W')

OOMP.parts.append(newPart)