###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "B3F-40XX-ROUND")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/B3F-40XX-ROUND")

newPart.addTag("description", """&lt;b&gt;OMRON SWITCH&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-B3F-40XX-ROUND",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='B3F-40XX-ROUND')

OOMP.parts.append(newPart)