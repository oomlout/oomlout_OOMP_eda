###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "CHIPLED_1206")
newPart.addTag("oompName", "eagle-default/ref-packages/CHIPLED_1206")

newPart.addTag("description", """&lt;b&gt;CHIPLED&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.osram.convergy.de/ ... LG_LY N971.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-CHIPLED_1206",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='CHIPLED_1206')

OOMP.parts.append(newPart)