###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "SOIC8_208MIL")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/SOIC8_208MIL")

newPart.addTag("description", """&lt;b&gt;Small Outline IC - 208mil Wide&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-SOIC8_208MIL",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='SOIC8_208MIL')

OOMP.parts.append(newPart)