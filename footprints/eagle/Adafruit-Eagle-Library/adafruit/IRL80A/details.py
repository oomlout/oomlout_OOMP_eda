###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "IRL80A")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/IRL80A")

newPart.addTag("description", """&lt;B&gt;IR LED&lt;/B&gt;&lt;p&gt;
IR transmitter Siemens""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-IRL80A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='IRL80A')

OOMP.parts.append(newPart)