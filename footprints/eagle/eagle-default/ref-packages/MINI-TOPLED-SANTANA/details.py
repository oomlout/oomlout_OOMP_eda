###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MINI-TOPLED-SANTANA")
newPart.addTag("oompName", "eagle-default/ref-packages/MINI-TOPLED-SANTANA")

newPart.addTag("description", """&lt;b&gt;Mini TOPLED Santana&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.osram.convergy.de/ ... LG M470.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MINI-TOPLED-SANTANA",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MINI-TOPLED-SANTANA')

OOMP.parts.append(newPart)