###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "PSO28")
newPart.addTag("oompName", "eagle-default/ref-packages/PSO28")

newPart.addTag("description", """&lt;b&gt;PLASTIC SMALL-OUTLINE PACKAGE&lt;/b&gt;&lt;p&gt;&#xD;
PW (R-PDSO-G**)&lt;br&gt;&#xD;
www.ti.com; tas3001.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-PSO28",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='PSO28')

OOMP.parts.append(newPart)