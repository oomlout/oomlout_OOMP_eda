###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "YC15B6")
newPart.addTag("oompName", "eagle-default/ref-packages/YC15B6")

newPart.addTag("description", """&lt;b&gt;Y CAPACITOR&lt;/b&gt;&lt;p&gt;&#xD;
body 17.7 x 6 mm, grid 15 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-YC15B6",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='YC15B6')

OOMP.parts.append(newPart)