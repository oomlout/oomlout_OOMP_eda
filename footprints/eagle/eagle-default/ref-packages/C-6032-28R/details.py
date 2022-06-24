###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "C/6032-28R")
newPart.addTag("oompName", "eagle-default/ref-packages/C/6032-28R")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET C / EIA 6032-28 Reflow solder&lt;/b&gt;&lt;p&gt;&#xD;
KEMET U / EIA 6032-15""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-C/6032-28R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='C/6032-28R')

OOMP.parts.append(newPart)