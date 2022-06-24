###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "SEGMENT_BICOL_BL-AR12Z3010")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/SEGMENT_BICOL_BL-AR12Z3010")

newPart.addTag("description", """&lt;b&gt;Souce: &lt;/b&gt;http://www.betlux.com/product/LED_light_bar/BL-AR12B3010xx.PDF""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-SEGMENT_BICOL_BL-AR12Z3010",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='SEGMENT_BICOL_BL-AR12Z3010')

OOMP.parts.append(newPart)