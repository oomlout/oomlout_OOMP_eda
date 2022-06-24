###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "YC12B5")
newPart.addTag("oompName", "eagle-default/ref-packages/YC12B5")

newPart.addTag("description", """&lt;b&gt;Y CAPACITOR&lt;/b&gt;&lt;p&gt;&#xD;
body 16.5 x 5 mm, grid 12.6 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-YC12B5",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='YC12B5')

OOMP.parts.append(newPart)