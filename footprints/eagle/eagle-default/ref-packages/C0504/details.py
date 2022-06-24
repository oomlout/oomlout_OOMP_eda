###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "C0504")
newPart.addTag("oompName", "eagle-default/ref-packages/C0504")

newPart.addTag("description", """&lt;b&gt;CAPACITOR&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-C0504",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='C0504')

OOMP.parts.append(newPart)