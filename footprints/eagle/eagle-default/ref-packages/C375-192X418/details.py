###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "C375-192X418")
newPart.addTag("oompName", "eagle-default/ref-packages/C375-192X418")

newPart.addTag("description", """&lt;b&gt;CAPACITOR&lt;/b&gt;&lt;p&gt;&#xD;
grid 37.5 mm, outline 19.2 x 41.8 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-C375-192X418",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='C375-192X418')

OOMP.parts.append(newPart)