###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MO023-50")
newPart.addTag("oompName", "eagle-default/ref-packages/MO023-50")

newPart.addTag("description", """&lt;b&gt;CFP50&lt;/b&gt;&lt;p&gt;&#xD;
ceramic flat pack""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MO023-50",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MO023-50')

OOMP.parts.append(newPart)