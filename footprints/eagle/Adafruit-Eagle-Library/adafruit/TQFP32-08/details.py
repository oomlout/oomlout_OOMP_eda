###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "TQFP32-08")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/TQFP32-08")

newPart.addTag("description", """&lt;B&gt;Thin Plasic Quad Flat Package&lt;/B&gt; Grid 0.8 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-TQFP32-08",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='TQFP32-08')

OOMP.parts.append(newPart)