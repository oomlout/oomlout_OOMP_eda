###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "ARDUINO")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/ARDUINO")

newPart.addTag("description", """&lt;b&gt;Arduino Uno&lt;/b&gt;
&lt;p&gt;
Make a shield with ease, this package has all the named pins as well as the two mounting drill holes and an outline of the USB and DC power connector. The outline is on the DIMENSION layer, so if your board house uses it they will cut the outline to match.""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-ARDUINO",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='ARDUINO')

OOMP.parts.append(newPart)