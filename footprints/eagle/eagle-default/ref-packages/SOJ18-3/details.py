###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOJ18-3")
newPart.addTag("oompName", "eagle-default/ref-packages/SOJ18-3")

newPart.addTag("description", """&lt;b&gt;SMALL OUTLINE J LEADS&lt;/b&gt;&lt;p&gt;&#xD;
body 8.88 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOJ18-3",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOJ18-3')

OOMP.parts.append(newPart)