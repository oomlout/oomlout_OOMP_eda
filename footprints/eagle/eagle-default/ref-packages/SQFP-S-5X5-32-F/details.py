###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SQFP-S-5X5-32-F")
newPart.addTag("oompName", "eagle-default/ref-packages/SQFP-S-5X5-32-F")

newPart.addTag("description", """&lt;b&gt;QFP32&lt;/b&gt;&lt;p&gt;&#xD;
shrink quad flat pack, square""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SQFP-S-5X5-32-F",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SQFP-S-5X5-32-F')

OOMP.parts.append(newPart)