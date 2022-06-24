###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "PBGA144")
newPart.addTag("oompName", "eagle-default/ref-packages/PBGA144")

newPart.addTag("description", """&lt;b&gt;PLASTIC BALL GRID ARRAY PACKAGE&lt;/b&gt;&lt;p&gt;&#xD;
GGU (S-PBGA-N144) Source: tms320vc5402.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-PBGA144",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='PBGA144')

OOMP.parts.append(newPart)