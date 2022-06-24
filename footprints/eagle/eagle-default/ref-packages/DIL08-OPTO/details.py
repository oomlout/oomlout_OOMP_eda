###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DIL08-OPTO")
newPart.addTag("oompName", "eagle-default/ref-packages/DIL08-OPTO")

newPart.addTag("description", """&lt;b&gt;Dula In Line&lt;/b&gt;&lt;p&gt;&#xD;
This dual-in-line package consists of an integrated circuit mounted on a lead frame and encapsulated with an&#xD;
electrically nonconductive clear plastic compound. The photodiode area is typically 1.36 mm2&lt;p&gt;&#xD;
from tsl230.pdf TAOS004 - MAY 1999""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DIL08-OPTO",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DIL08-OPTO')

OOMP.parts.append(newPart)