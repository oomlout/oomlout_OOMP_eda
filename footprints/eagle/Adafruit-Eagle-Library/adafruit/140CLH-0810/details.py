###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "140CLH-0810")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/140CLH-0810")

newPart.addTag("description", """&lt;b&gt;Aluminum electrolytic capacitors SMD (Chip)&lt;/b&gt;&lt;p&gt;
Long life base plate, High temperature 140 CLH&lt;p&gt;
http://www.bccomponents.com/""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-140CLH-0810",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='140CLH-0810')

OOMP.parts.append(newPart)