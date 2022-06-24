###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "H03A")
newPart.addTag("oompName", "eagle-default/ref-packages/H03A")

newPart.addTag("description", """&lt;b&gt;Metal Can Package&lt;/b&gt;&lt;p&gt;&#xD;
National Semiconductor H03A&lt;br&gt;&#xD;
Motorola 79-05""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-H03A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='H03A')

OOMP.parts.append(newPart)