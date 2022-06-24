###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "P-LCC-4")
newPart.addTag("oompName", "eagle-default/ref-packages/P-LCC-4")

newPart.addTag("description", """&lt;b&gt;Power TOPLED&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.osram.convergy.de/ ... LA_LO_LA_LY E67B.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-P-LCC-4",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='P-LCC-4')

OOMP.parts.append(newPart)