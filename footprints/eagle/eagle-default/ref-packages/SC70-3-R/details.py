###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SC70-3-R")
newPart.addTag("oompName", "eagle-default/ref-packages/SC70-3-R")

newPart.addTag("description", """&lt;b&gt;SC70-3 Reflow soldering&lt;/b&gt; Philips SC01_Mounting_1996.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SC70-3-R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SC70-3-R')

OOMP.parts.append(newPart)