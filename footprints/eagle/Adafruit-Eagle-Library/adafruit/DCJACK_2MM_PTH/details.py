###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "DCJACK_2MM_PTH")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/DCJACK_2MM_PTH")

newPart.addTag("description", """DJ Jack 2.0mm PTH Right-Angle""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-DCJACK_2MM_PTH",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='DCJACK_2MM_PTH')

OOMP.parts.append(newPart)