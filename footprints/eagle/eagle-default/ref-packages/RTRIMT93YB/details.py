###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIMT93YB")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIMT93YB")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; VISHAY&lt;p&gt;&#xD;
Cermet, abgedichtet nach IP67""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIMT93YB",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIMT93YB')

OOMP.parts.append(newPart)