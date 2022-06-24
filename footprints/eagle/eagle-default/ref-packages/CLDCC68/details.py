###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "CLDCC68")
newPart.addTag("oompName", "eagle-default/ref-packages/CLDCC68")

newPart.addTag("description", """&lt;b&gt;CERAMIC LEADED CHIP CARRIER&lt;/b&gt;&lt;p&gt;&#xD;
square""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-CLDCC68",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='CLDCC68')

OOMP.parts.append(newPart)