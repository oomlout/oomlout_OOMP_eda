###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DO-214BA")
newPart.addTag("oompName", "eagle-default/ref-packages/DO-214BA")

newPart.addTag("description", """&lt;b&gt;GF1&lt;/b&gt;&lt;p&gt;&#xD;
General Semiconductor""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DO-214BA",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DO-214BA')

OOMP.parts.append(newPart)