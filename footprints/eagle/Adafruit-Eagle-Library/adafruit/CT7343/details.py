###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "CT7343")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/CT7343")

newPart.addTag("description", """&lt;b&gt;CAPACITOR&lt;/b&gt;&lt;p&gt;
chip
tantalum""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-CT7343",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='CT7343')

OOMP.parts.append(newPart)