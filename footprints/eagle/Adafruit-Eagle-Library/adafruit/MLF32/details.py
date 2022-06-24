###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "MLF32")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/MLF32")

newPart.addTag("description", """&lt;b&gt;32M1-A&lt;/b&gt; Micro Lead Frame package (MLF)&lt;p&gt;
Source: http://www.atmel.com .. doc1477.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-MLF32",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='MLF32')

OOMP.parts.append(newPart)