###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "VMT3")
newPart.addTag("oompName", "eagle-default/ref-packages/VMT3")

newPart.addTag("description", """&lt;b&gt;ROHM : VMT3&lt;/b&gt;&lt;p&gt;&#xD;
2SC4726.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-VMT3",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='VMT3')

OOMP.parts.append(newPart)