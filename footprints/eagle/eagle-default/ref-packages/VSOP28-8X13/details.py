###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "VSOP28-8X13")
newPart.addTag("oompName", "eagle-default/ref-packages/VSOP28-8X13")

newPart.addTag("description", """&lt;b&gt;Very Small Outline Package&lt;/b&gt;&lt;p&gt;&#xD;
8 x 13.4 mm, package type VS""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-VSOP28-8X13",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='VSOP28-8X13')

OOMP.parts.append(newPart)