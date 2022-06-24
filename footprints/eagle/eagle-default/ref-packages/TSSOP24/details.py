###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TSSOP24")
newPart.addTag("oompName", "eagle-default/ref-packages/TSSOP24")

newPart.addTag("description", """&lt;b&gt;Thin Shrink Small Outline Plastic 24&lt;/b&gt;&lt;p&gt;&#xD;
MAX3223-MAX3243.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TSSOP24",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TSSOP24')

OOMP.parts.append(newPart)