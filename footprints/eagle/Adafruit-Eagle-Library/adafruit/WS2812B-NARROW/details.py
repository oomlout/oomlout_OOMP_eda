###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "WS2812B-NARROW")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/WS2812B-NARROW")


newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-WS2812B-NARROW",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='WS2812B-NARROW')

OOMP.parts.append(newPart)