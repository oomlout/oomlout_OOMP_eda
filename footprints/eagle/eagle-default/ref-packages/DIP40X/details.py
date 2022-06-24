###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DIP40X")
newPart.addTag("oompName", "eagle-default/ref-packages/DIP40X")

newPart.addTag("description", """&lt;b&gt;SMD DIL40X&lt;/b&gt;&lt;p&gt;&#xD;
dual in line package, body 13.52 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DIP40X",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DIP40X')

OOMP.parts.append(newPart)