###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIMT18")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIMT18")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; VISHAY&lt;p&gt;&#xD;
abgedichtet nach IP67""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIMT18",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIMT18')

OOMP.parts.append(newPart)