###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "USB-MINIB-THM")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/USB-MINIB-THM")

newPart.addTag("description", """&lt;b&gt;Mini USB 5-pin thru-mount connector&lt;/b&gt;
&lt;p&gt;
4Ucon #18732""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-USB-MINIB-THM",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='USB-MINIB-THM')

OOMP.parts.append(newPart)