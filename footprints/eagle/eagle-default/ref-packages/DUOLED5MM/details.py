###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DUOLED5MM")
newPart.addTag("oompName", "eagle-default/ref-packages/DUOLED5MM")

newPart.addTag("description", """&lt;B&gt;DUO LED&lt;/B&gt;&lt;p&gt;&#xD;
2 colors, 5 mm, round""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DUOLED5MM",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DUOLED5MM')

OOMP.parts.append(newPart)