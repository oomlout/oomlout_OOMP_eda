###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SSOP24")
newPart.addTag("oompName", "eagle-default/ref-packages/SSOP24")

newPart.addTag("description", """&lt;b&gt;Small Shrink Outline Package&lt;/b&gt;&lt;p&gt;&#xD;
SOT340-1 / JEDEC MO-150AG""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SSOP24",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SSOP24')

OOMP.parts.append(newPart)