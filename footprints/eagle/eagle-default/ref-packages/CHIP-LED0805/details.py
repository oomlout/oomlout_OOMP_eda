###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "CHIP-LED0805")
newPart.addTag("oompName", "eagle-default/ref-packages/CHIP-LED0805")

newPart.addTag("description", """&lt;b&gt;Hyper CHIPLED Hyper-Bright LED&lt;/b&gt;&lt;p&gt;&#xD;
LB R99A&lt;br&gt;&#xD;
Source: http://www.osram.convergy.de/ ... lb_r99a.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-CHIP-LED0805",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='CHIP-LED0805')

OOMP.parts.append(newPart)