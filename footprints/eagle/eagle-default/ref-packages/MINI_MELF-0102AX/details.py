###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MINI_MELF-0102AX")
newPart.addTag("oompName", "eagle-default/ref-packages/MINI_MELF-0102AX")

newPart.addTag("description", """&lt;b&gt;Mini MELF 0102 Axial&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MINI_MELF-0102AX",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MINI_MELF-0102AX')

OOMP.parts.append(newPart)