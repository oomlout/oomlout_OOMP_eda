###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOJ28-45")
newPart.addTag("oompName", "eagle-default/ref-packages/SOJ28-45")

newPart.addTag("description", """&lt;b&gt;SMALL OUTLINE J LEADS&lt;/b&gt;&lt;p&gt;&#xD;
body 11.38 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOJ28-45",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOJ28-45')

OOMP.parts.append(newPart)