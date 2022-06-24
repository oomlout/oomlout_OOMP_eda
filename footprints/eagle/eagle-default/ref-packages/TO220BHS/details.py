###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TO220BHS")
newPart.addTag("oompName", "eagle-default/ref-packages/TO220BHS")

newPart.addTag("description", """&lt;b&gt;Molded Package&lt;/b&gt;&lt;p&gt;&#xD;
grid 2.54 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TO220BHS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TO220BHS')

OOMP.parts.append(newPart)