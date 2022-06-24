###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MULTIWAT-SIL17")
newPart.addTag("oompName", "eagle-default/ref-packages/MULTIWAT-SIL17")

newPart.addTag("description", """&lt;b&gt;DBS17P&lt;/b&gt; plastic DIL-bent-SIL power package&lt;p&gt;&#xD;
17 leads (lead length 12 mm) SOT243-1""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MULTIWAT-SIL17",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MULTIWAT-SIL17')

OOMP.parts.append(newPart)