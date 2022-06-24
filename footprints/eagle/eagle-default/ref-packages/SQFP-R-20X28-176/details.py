###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SQFP-R-20X28-176")
newPart.addTag("oompName", "eagle-default/ref-packages/SQFP-R-20X28-176")

newPart.addTag("description", """&lt;b&gt;QFP176&lt;/b&gt;&lt;p&gt;&#xD;
shrink quad flat pack, rectangle""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SQFP-R-20X28-176",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SQFP-R-20X28-176')

OOMP.parts.append(newPart)