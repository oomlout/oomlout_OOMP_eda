###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "EMT3")
newPart.addTag("oompName", "eagle-default/ref-packages/EMT3")

newPart.addTag("description", """&lt;b&gt;ROHM : EMT3 ; EIAJ : SC-75A&lt;p&gt;&#xD;
2SC4726.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-EMT3",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='EMT3')

OOMP.parts.append(newPart)