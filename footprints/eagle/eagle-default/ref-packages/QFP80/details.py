###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "QFP80")
newPart.addTag("oompName", "eagle-default/ref-packages/QFP80")

newPart.addTag("description", """&lt;b&gt;80-Pin QFP&lt;/b&gt; (Case no. 841B)&lt;p&gt;&#xD;
9S12A256DGV1.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-QFP80",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='QFP80')

OOMP.parts.append(newPart)