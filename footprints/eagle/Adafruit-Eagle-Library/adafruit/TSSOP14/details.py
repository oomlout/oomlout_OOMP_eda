###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "TSSOP14")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/TSSOP14")

newPart.addTag("description", """&lt;b&gt;Thin Shrink Small Outline Plastic 14&lt;/b&gt;&lt;p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-TSSOP14",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='TSSOP14')

OOMP.parts.append(newPart)