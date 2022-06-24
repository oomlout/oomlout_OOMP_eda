###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "SSOP28")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/SSOP28")

newPart.addTag("description", """&lt;b&gt;Shrink Small Outline Package&lt;/b&gt;&lt;p&gt;
package type SS""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-SSOP28",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='SSOP28')

OOMP.parts.append(newPart)