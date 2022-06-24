###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "B/3528-21R")
newPart.addTag("oompName", "eagle-default/ref-packages/B/3528-21R")

newPart.addTag("description", """&lt;b&gt;Chip Capacitor Type KEMET B / EIA 3528-21 Reflow solder&lt;/b&gt;&lt;p&gt;&#xD;
KEMET T / EIA 3528-12""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-B/3528-21R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='B/3528-21R')

OOMP.parts.append(newPart)