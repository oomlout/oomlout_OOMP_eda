###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MICRO-SIDELED")
newPart.addTag("oompName", "eagle-default/ref-packages/MICRO-SIDELED")

newPart.addTag("description", """&lt;b&gt;Hyper Micro SIDELED&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.osram.convergy.de/ ... LA_LO_LS_LY Y876.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MICRO-SIDELED",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MICRO-SIDELED')

OOMP.parts.append(newPart)