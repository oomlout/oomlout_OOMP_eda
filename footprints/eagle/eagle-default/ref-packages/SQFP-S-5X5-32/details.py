###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SQFP-S-5X5-32")
newPart.addTag("oompName", "eagle-default/ref-packages/SQFP-S-5X5-32")

newPart.addTag("description", """&lt;b&gt;QFP32&lt;/b&gt;&lt;p&gt;&#xD;
shrink quad flat pack, square""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SQFP-S-5X5-32",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SQFP-S-5X5-32')

OOMP.parts.append(newPart)