###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "C1702-05")
newPart.addTag("oompName", "eagle-default/ref-packages/C1702-05")

newPart.addTag("description", """&lt;B&gt;DIODE&lt;/B&gt;&lt;p&gt;&#xD;
diameter 3.5 mm, vertical, grid 5.08 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-C1702-05",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='C1702-05')

OOMP.parts.append(newPart)