###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "139CLL-3W")
newPart.addTag("oompName", "eagle-default/ref-packages/139CLL-3W")

newPart.addTag("description", """&lt;b&gt;Aluminum electrolytic capacitors&lt;/b&gt; wave soldering&lt;p&gt;&#xD;
SMD (Chip) Long Life 139 CLL&lt;p&gt;&#xD;
http://www.bccomponents.com/""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-139CLL-3W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='139CLL-3W')

OOMP.parts.append(newPart)