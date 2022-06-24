###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "139CLL-2R")
newPart.addTag("oompName", "eagle-default/ref-packages/139CLL-2R")

newPart.addTag("description", """&lt;b&gt;Aluminum electrolytic capacitors&lt;/b&gt; reflow soldering&lt;p&gt;&#xD;
SMD (Chip) Long Life 139 CLL&lt;p&gt;&#xD;
http://www.bccomponents.com/""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-139CLL-2R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='139CLL-2R')

OOMP.parts.append(newPart)