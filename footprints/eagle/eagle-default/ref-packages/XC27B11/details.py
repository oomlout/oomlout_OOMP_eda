###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "XC27B11")
newPart.addTag("oompName", "eagle-default/ref-packages/XC27B11")

newPart.addTag("description", """&lt;b&gt;X CAPACITOR&lt;/b&gt;&lt;p&gt;&#xD;
body 32 x 11 mm, grid 27.9 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-XC27B11",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='XC27B11')

OOMP.parts.append(newPart)