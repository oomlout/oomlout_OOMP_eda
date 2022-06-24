###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "C050-045X075")
newPart.addTag("oompName", "eagle-default/ref-packages/C050-045X075")

newPart.addTag("description", """&lt;b&gt;CAPACITOR&lt;/b&gt;&lt;p&gt;&#xD;
grid 5 mm, outline 4.5 x 7.5 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-C050-045X075",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='C050-045X075')

OOMP.parts.append(newPart)