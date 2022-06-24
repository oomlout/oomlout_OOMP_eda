###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "P2-15")
newPart.addTag("oompName", "eagle-default/ref-packages/P2-15")

newPart.addTag("description", """&lt;B&gt;DIODE&lt;/B&gt;&lt;p&gt;&#xD;
diameter 5 mm, horizontal, grid 12.7 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-P2-15",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='P2-15')

OOMP.parts.append(newPart)