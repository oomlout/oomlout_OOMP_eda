###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "XF2R-4015-4A")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/XF2R-4015-4A")

newPart.addTag("description", """&lt;b&gt;Low-profile Rotary Backlock Type (0.5 mm-pitch)&lt;/b&gt;&lt;p&gt;Source : http://www.omron.com/ecb/products/pdf/fpc.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-XF2R-4015-4A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='XF2R-4015-4A')

OOMP.parts.append(newPart)