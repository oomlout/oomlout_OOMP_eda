###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DIP24L")
newPart.addTag("oompName", "eagle-default/ref-packages/DIP24L")

newPart.addTag("description", """&lt;b&gt;SMD DIL24L&lt;/b&gt;&lt;p&gt;&#xD;
dual in line package, body 9.02 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DIP24L",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DIP24L')

OOMP.parts.append(newPart)