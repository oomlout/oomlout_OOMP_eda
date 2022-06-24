###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "XF2L-0535-1")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/XF2L-0535-1")

newPart.addTag("description", """&lt;b&gt;ZIF Slide-locking Type (0.5 mm-pitch)&lt;/b&gt; Lower-contact Type&lt;p&gt;
Source : http://www.omron.com/ecb/products/pdf/fpc.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-XF2L-0535-1",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='XF2L-0535-1')

OOMP.parts.append(newPart)