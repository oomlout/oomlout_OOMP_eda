###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "SEGMENT_BICOL_BL-M12A883XX")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/SEGMENT_BICOL_BL-M12A883XX")

newPart.addTag("description", """&lt;b&gt;Source: &lt;/b&gt;http://www.betlux.com/product/led_dot_matrix/BL-M12A883xx.PDF""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-SEGMENT_BICOL_BL-M12A883XX",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='SEGMENT_BICOL_BL-M12A883XX')

OOMP.parts.append(newPart)