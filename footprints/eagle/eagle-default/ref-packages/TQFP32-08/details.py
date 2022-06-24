###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TQFP32-08")
newPart.addTag("oompName", "eagle-default/ref-packages/TQFP32-08")

newPart.addTag("description", """&lt;B&gt;Thin Plasic Quad Flat Package&lt;/B&gt; Grid 0.8 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TQFP32-08",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TQFP32-08')

OOMP.parts.append(newPart)