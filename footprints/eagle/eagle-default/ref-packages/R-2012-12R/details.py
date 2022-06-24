###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "R/2012-12R")
newPart.addTag("oompName", "eagle-default/ref-packages/R/2012-12R")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET R/EIA 2012-12 Reflow solder&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-R/2012-12R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='R/2012-12R')

OOMP.parts.append(newPart)