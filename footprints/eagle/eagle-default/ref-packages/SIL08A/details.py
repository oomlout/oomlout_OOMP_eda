###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SIL08A")
newPart.addTag("oompName", "eagle-default/ref-packages/SIL08A")

newPart.addTag("description", """7 &lt;B&gt;DIODES&lt;/B&gt;&lt;p&gt;&#xD;
single in line 7 diodes with common anode""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SIL08A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SIL08A')

OOMP.parts.append(newPart)