###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "ILI9325_28INCH_TS")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/ILI9325_28INCH_TS")

newPart.addTag("description", """1.0mm-Pitch 37 Pin LCD Connector""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-ILI9325_28INCH_TS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='ILI9325_28INCH_TS')

OOMP.parts.append(newPart)