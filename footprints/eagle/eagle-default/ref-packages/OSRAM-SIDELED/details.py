###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "OSRAM-SIDELED")
newPart.addTag("oompName", "eagle-default/ref-packages/OSRAM-SIDELED")

newPart.addTag("description", """&lt;b&gt;Super SIDELED High-Current LED&lt;/b&gt;&lt;p&gt;&#xD;
LG A672, LP A672 &lt;br&gt;&#xD;
Source: http://www.osram.convergy.de/ ... l_a672.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-OSRAM-SIDELED",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='OSRAM-SIDELED')

OOMP.parts.append(newPart)