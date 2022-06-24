###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "C2220K")
newPart.addTag("oompName", "eagle-default/ref-packages/C2220K")

newPart.addTag("description", """&lt;b&gt;Ceramic Chip Capacitor KEMET 2220 Reflow solder&lt;/b&gt;&lt;p&gt;&#xD;
Metric Code Size 5650""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-C2220K",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='C2220K')

OOMP.parts.append(newPart)