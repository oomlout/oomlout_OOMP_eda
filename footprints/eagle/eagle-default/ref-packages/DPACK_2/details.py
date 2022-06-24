###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DPACK_2")
newPart.addTag("oompName", "eagle-default/ref-packages/DPACK_2")

newPart.addTag("description", """&lt;b&gt;DPAK&lt;/b&gt;&lt;p&gt;Style 2 (Motorola)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DPACK_2",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DPACK_2')

OOMP.parts.append(newPart)