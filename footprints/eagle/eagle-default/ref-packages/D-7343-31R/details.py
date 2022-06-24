###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "D/7343-31R")
newPart.addTag("oompName", "eagle-default/ref-packages/D/7343-31R")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET D / EIA 7343-21&lt;/b&gt;&lt;p&gt;&#xD;
KEMET V / EIA 7343-20, KEMET X / EIA 7343-43 Reflow solder""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-D/7343-31R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='D/7343-31R')

OOMP.parts.append(newPart)