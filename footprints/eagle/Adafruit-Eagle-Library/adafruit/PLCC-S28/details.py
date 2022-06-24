###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "PLCC-S28")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/PLCC-S28")

newPart.addTag("description", """&lt;b&gt;Plastic Leaded Chip Carrier&lt;/b&gt; Socked""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-PLCC-S28",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='PLCC-S28')

OOMP.parts.append(newPart)