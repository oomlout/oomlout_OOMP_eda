###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "LED2X5")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/LED2X5")

newPart.addTag("description", """&lt;B&gt;LED&lt;/B&gt;&lt;p&gt;
2 x 5 mm, rectangle""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-LED2X5",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='LED2X5')

OOMP.parts.append(newPart)