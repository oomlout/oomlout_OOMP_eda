###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "HSOP")
newPart.addTag("oompName", "eagle-default/ref-packages/HSOP")

newPart.addTag("description", """&lt;b&gt;Heatsink Small Outline Package (HSOP)&lt;/b&gt;&lt;p&gt;&#xD;
Source: www.motorola.com/... AN2388.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-HSOP",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='HSOP')

OOMP.parts.append(newPart)