###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIM3214W")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIM3214W")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; BOURNS&lt;p&gt;&#xD;
SMD Cermet trimmer""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIM3214W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIM3214W')

OOMP.parts.append(newPart)