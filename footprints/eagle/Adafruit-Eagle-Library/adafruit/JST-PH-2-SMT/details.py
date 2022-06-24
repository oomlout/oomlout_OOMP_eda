###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "JST-PH-2-SMT")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/JST-PH-2-SMT")

newPart.addTag("description", """2-Pin JST PH Series Right-Angle Connector (+/- for batteries)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-JST-PH-2-SMT",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='JST-PH-2-SMT')

OOMP.parts.append(newPart)