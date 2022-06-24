###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SIL05C")
newPart.addTag("oompName", "eagle-default/ref-packages/SIL05C")

newPart.addTag("description", """4 &lt;B&gt;DIODES&lt;/B&gt;&lt;p&gt;&#xD;
single in line 4 diodes with common cathode""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SIL05C",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SIL05C')

OOMP.parts.append(newPart)