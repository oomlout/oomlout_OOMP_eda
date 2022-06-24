###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "JST-PH-2-THM-RA")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/JST-PH-2-THM-RA")

newPart.addTag("description", """&lt;b&gt;S2B-PH-K-S&lt;/b&gt; 
&lt;p&gt;
JST PH 2-pin thru-home side entry""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-JST-PH-2-THM-RA",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='JST-PH-2-THM-RA')

OOMP.parts.append(newPart)