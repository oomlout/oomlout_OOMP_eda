###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "H10C")
newPart.addTag("oompName", "eagle-default/ref-packages/H10C")

newPart.addTag("description", """&lt;b&gt;Metal Can Package&lt;/b&gt;&lt;p&gt;&#xD;
National Semiconductor H10C&lt;br&gt;&#xD;
Motorola 603-04 / 603C-01""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-H10C",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='H10C')

OOMP.parts.append(newPart)