###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "XC15B5")
newPart.addTag("oompName", "eagle-default/ref-packages/XC15B5")

newPart.addTag("description", """&lt;b&gt;X CAPACITOR&lt;/b&gt;&lt;p&gt;&#xD;
body 17.5 x 5 mm, grid 15.24 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-XC15B5",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='XC15B5')

OOMP.parts.append(newPart)