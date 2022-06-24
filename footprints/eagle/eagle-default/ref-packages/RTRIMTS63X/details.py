###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIMTS63X")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIMTS63X")

newPart.addTag("description", """&lt;b&gt;Trimm resistror&lt;/b&gt; VISHAY&lt;p&gt;&#xD;
seales container, solder immerson IP67""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIMTS63X",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIMTS63X')

OOMP.parts.append(newPart)