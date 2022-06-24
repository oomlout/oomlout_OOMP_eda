###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "LQFP80")
newPart.addTag("oompName", "eagle-default/ref-packages/LQFP80")

newPart.addTag("description", """&lt;b&gt;80 Lead LQFP_ED (SQ-80) (ST-80)&lt;/b&gt;&lt;p&gt;&#xD;
www.analog.com AD9852_b.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-LQFP80",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='LQFP80')

OOMP.parts.append(newPart)