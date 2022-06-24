###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TO220AH")
newPart.addTag("oompName", "eagle-default/ref-packages/TO220AH")

newPart.addTag("description", """&lt;b&gt;Molded Package&lt;/b&gt;&lt;p&gt;&#xD;
grid 2.54 - 5.08 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TO220AH",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TO220AH')

OOMP.parts.append(newPart)