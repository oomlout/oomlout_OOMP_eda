###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SIL09A")
newPart.addTag("oompName", "eagle-default/ref-packages/SIL09A")

newPart.addTag("description", """8 &lt;B&gt;DIODES&lt;/B&gt;&lt;p&gt;&#xD;
single in line 8 diodes with common anode""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SIL09A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SIL09A')

OOMP.parts.append(newPart)