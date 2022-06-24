###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "LCC20C")
newPart.addTag("oompName", "eagle-default/ref-packages/LCC20C")

newPart.addTag("description", """&lt;b&gt;LEADED CHIP CARRIER&lt;/b&gt;&lt;p&gt;&#xD;
rectangle""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-LCC20C",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='LCC20C')

OOMP.parts.append(newPart)