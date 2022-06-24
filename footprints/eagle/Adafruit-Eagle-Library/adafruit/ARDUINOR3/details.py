###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "ARDUINOR3")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/ARDUINOR3")

newPart.addTag("description", """The new Arduino R3 'classic' adds duplicate I2C pins and an IORef pin (and an unused pin""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-ARDUINOR3",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='ARDUINOR3')

OOMP.parts.append(newPart)