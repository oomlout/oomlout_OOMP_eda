###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "0204/5")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/0204/5")

newPart.addTag("description", """&lt;b&gt;RESISTOR&lt;/b&gt;&lt;p&gt;
type 0204, grid 5 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-0204/5",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='0204/5')

OOMP.parts.append(newPart)