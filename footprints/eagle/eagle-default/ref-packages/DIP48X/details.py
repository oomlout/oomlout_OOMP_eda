###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DIP48X")
newPart.addTag("oompName", "eagle-default/ref-packages/DIP48X")

newPart.addTag("description", """&lt;b&gt;SMD DIL48X&lt;/b&gt;&lt;p&gt;&#xD;
dual in line package, body 13.52 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DIP48X",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DIP48X')

OOMP.parts.append(newPart)