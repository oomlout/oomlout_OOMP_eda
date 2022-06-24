###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "P6T15")
newPart.addTag("oompName", "eagle-default/ref-packages/P6T15")

newPart.addTag("description", """&lt;B&gt;DIODE&lt;/B&gt;&lt;p&gt;&#xD;
diameter 9 mm, horizontal, grid 15.24 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-P6T15",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='P6T15')

OOMP.parts.append(newPart)