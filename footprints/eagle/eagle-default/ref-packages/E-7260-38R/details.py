###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "E/7260-38R")
newPart.addTag("oompName", "eagle-default/ref-packages/E/7260-38R")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET E / EIA 7260-38 Reflow solder&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-E/7260-38R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='E/7260-38R')

OOMP.parts.append(newPart)