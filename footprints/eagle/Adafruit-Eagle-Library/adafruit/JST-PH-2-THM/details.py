###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "JST-PH-2-THM")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/JST-PH-2-THM")

newPart.addTag("description", """4UCon #01528
http://www.4uconnector.com/online/object/4udrawing/01528.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-JST-PH-2-THM",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='JST-PH-2-THM')

OOMP.parts.append(newPart)