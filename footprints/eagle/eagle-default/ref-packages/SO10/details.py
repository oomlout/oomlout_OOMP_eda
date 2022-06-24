###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SO10")
newPart.addTag("oompName", "eagle-default/ref-packages/SO10")

newPart.addTag("description", """&lt;b&gt;10-Lead Mini_SO Package&lt;/b&gt;&lt;p&gt;&#xD;
(RM-10)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SO10",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SO10')

OOMP.parts.append(newPart)