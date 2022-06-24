###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOJ16-35")
newPart.addTag("oompName", "eagle-default/ref-packages/SOJ16-35")

newPart.addTag("description", """&lt;b&gt;SMALL OUTLINE J LEADS&lt;/b&gt;&lt;p&gt;&#xD;
body 8.88 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOJ16-35",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOJ16-35')

OOMP.parts.append(newPart)