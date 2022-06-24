###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SSO64")
newPart.addTag("oompName", "eagle-default/ref-packages/SSO64")

newPart.addTag("description", """&lt;b&gt;SSO64&lt;/b&gt;&lt;p&gt;&#xD;
small outline integrated circuit/JEDEC M-0117""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SSO64",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SSO64')

OOMP.parts.append(newPart)