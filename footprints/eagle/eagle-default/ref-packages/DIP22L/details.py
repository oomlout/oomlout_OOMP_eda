###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DIP22L")
newPart.addTag("oompName", "eagle-default/ref-packages/DIP22L")

newPart.addTag("description", """&lt;b&gt;SMD DIL22&lt;/b&gt;&lt;p&gt;&#xD;
dual in line package, body 9 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DIP22L",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DIP22L')

OOMP.parts.append(newPart)