###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TO202BV")
newPart.addTag("oompName", "eagle-default/ref-packages/TO202BV")

newPart.addTag("description", """&lt;b&gt;Molded Package&lt;/b&gt;&lt;p&gt;&#xD;
grid 2.54 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TO202BV",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TO202BV')

OOMP.parts.append(newPart)