###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TSOP8X14")
newPart.addTag("oompName", "eagle-default/ref-packages/TSOP8X14")

newPart.addTag("description", """&lt;b&gt;TSOP24&lt;/b&gt;&lt;p&gt;&#xD;
thin small outline package""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TSOP8X14",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TSOP8X14')

OOMP.parts.append(newPart)