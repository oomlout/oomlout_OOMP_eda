###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DPACK_5")
newPart.addTag("oompName", "eagle-default/ref-packages/DPACK_5")

newPart.addTag("description", """&lt;b&gt;DPAK&lt;/b&gt;&lt;p&gt;Style 5 (Motorola)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DPACK_5",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DPACK_5')

OOMP.parts.append(newPart)