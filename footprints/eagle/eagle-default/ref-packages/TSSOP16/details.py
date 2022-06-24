###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TSSOP16")
newPart.addTag("oompName", "eagle-default/ref-packages/TSSOP16")

newPart.addTag("description", """&lt;b&gt;Thin Shrink Small Outline Plastic 16&lt;/b&gt;&lt;p&gt;&#xD;
MAX3223-MAX3243.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TSSOP16",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TSSOP16')

OOMP.parts.append(newPart)