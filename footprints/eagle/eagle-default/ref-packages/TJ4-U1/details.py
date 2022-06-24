###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TJ4-U1")
newPart.addTag("oompName", "eagle-default/ref-packages/TJ4-U1")

newPart.addTag("description", """&lt;b&gt;Inductor&lt;/b&gt;&lt;p&gt;&#xD;
Source: TJ-Serie Vishay.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TJ4-U1",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TJ4-U1')

OOMP.parts.append(newPart)