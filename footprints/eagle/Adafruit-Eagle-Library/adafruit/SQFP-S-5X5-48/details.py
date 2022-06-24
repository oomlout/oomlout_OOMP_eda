###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "SQFP-S-5X5-48")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/SQFP-S-5X5-48")

newPart.addTag("description", """&lt;b&gt;QFP48&lt;/b&gt;&lt;p&gt;
shrink quad flat pack, square""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-SQFP-S-5X5-48",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='SQFP-S-5X5-48')

OOMP.parts.append(newPart)