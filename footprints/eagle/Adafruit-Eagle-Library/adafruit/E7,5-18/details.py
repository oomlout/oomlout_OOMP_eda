###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "E7,5-18")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/E7,5-18")

newPart.addTag("description", """&lt;b&gt;ELECTROLYTIC CAPACITOR&lt;/b&gt;&lt;p&gt;
grid 7.62 mm, diameter 18 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-E7,5-18",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='E7,5-18')

OOMP.parts.append(newPart)