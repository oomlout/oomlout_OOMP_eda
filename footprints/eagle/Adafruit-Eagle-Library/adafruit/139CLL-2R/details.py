###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "139CLL-2R")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/139CLL-2R")

newPart.addTag("description", """&lt;b&gt;Aluminum electrolytic capacitors&lt;/b&gt; reflow soldering&lt;p&gt;
SMD (Chip) Long Life 139 CLL&lt;p&gt;
http://www.bccomponents.com/""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-139CLL-2R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='139CLL-2R')

OOMP.parts.append(newPart)