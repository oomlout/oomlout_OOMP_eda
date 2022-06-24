###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "150CLZ-0810")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/150CLZ-0810")

newPart.addTag("description", """&lt;b&gt;Aluminum electrolytic capacitors SMD (Chip)&lt;/b&gt;&lt;p&gt;
Long life base plate, very low impedance 150 CLZ&lt;p&gt;
http://www.bccomponents.com/""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-150CLZ-0810",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='150CLZ-0810')

OOMP.parts.append(newPart)