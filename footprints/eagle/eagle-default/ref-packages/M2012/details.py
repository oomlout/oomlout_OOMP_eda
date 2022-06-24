###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "M2012")
newPart.addTag("oompName", "eagle-default/ref-packages/M2012")

newPart.addTag("description", """&lt;b&gt;RESISTOR&lt;/b&gt;&lt;p&gt;&#xD;
MELF 0.10 W""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-M2012",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='M2012')

OOMP.parts.append(newPart)