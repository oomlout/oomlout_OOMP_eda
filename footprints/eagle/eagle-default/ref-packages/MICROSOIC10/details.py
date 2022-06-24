###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MICROSOIC10")
newPart.addTag("oompName", "eagle-default/ref-packages/MICROSOIC10")

newPart.addTag("description", """&lt;b&gt;10-Lead microSOIC&lt;/b&gt;&lt;p&gt;&#xD;
(RM-10) 10-SOIC""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MICROSOIC10",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MICROSOIC10')

OOMP.parts.append(newPart)