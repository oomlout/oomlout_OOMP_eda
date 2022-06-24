###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "L4035M")
newPart.addTag("oompName", "eagle-default/ref-packages/L4035M")

newPart.addTag("description", """&lt;b&gt;INDUCTOR&lt;/b&gt;&lt;p&gt;&#xD;
molded""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-L4035M",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='L4035M')

OOMP.parts.append(newPart)