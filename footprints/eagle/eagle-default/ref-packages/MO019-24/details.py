###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MO019-24")
newPart.addTag("oompName", "eagle-default/ref-packages/MO019-24")

newPart.addTag("description", """&lt;b&gt;CFP24&lt;/b&gt;&lt;p&gt;&#xD;
ceramic flat pack""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MO019-24",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MO019-24')

OOMP.parts.append(newPart)