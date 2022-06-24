###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "D2PACK")
newPart.addTag("oompName", "eagle-default/ref-packages/D2PACK")

newPart.addTag("description", """&lt;b&gt;D2PACK&lt;/b&gt;&lt;p&gt;&#xD;
INTERNATIONAL RECTIFIER, irg4bc15ud-s.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-D2PACK",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='D2PACK')

OOMP.parts.append(newPart)