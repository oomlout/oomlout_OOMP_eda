###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "QFN28-ML_6X6MM")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/QFN28-ML_6X6MM")

newPart.addTag("description", """&lt;b&gt;QFN28-ML_6X6MM&lt;/b&gt;&lt;p&gt;
Source: http://www.microchip.com .. 39637a.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-QFN28-ML_6X6MM",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='QFN28-ML_6X6MM')

OOMP.parts.append(newPart)