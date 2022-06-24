###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SSO56")
newPart.addTag("oompName", "eagle-default/ref-packages/SSO56")

newPart.addTag("description", """&lt;b&gt;SSO56&lt;/b&gt;&lt;p&gt;&#xD;
small outline integrated circuit/JEDEC MO-118AB""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SSO56",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SSO56')

OOMP.parts.append(newPart)