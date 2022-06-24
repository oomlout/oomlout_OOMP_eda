###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "SEGMENT_BL-M12A883")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/SEGMENT_BL-M12A883")

newPart.addTag("description", """&lt;b&gt;Source:&lt;/b&gt; http://www.betlux.com/product/LED_dot_matrix/BL-M12A883.PDF""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-SEGMENT_BL-M12A883",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='SEGMENT_BL-M12A883')

OOMP.parts.append(newPart)