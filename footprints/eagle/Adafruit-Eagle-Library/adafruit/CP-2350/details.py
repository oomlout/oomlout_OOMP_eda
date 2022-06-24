###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "CP-2350")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/CP-2350")

newPart.addTag("description", """Female &lt;b&gt;CONNECTOR&lt;/b&gt;&lt;p&gt;
5 pins 90 deg. with shield, horizontal (DIN 41524)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-CP-2350",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='CP-2350')

OOMP.parts.append(newPart)