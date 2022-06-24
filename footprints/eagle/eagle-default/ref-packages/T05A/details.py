###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "T05A")
newPart.addTag("oompName", "eagle-default/ref-packages/T05A")

newPart.addTag("description", """&lt;b&gt;TO-220&lt;/b&gt; 5 lead&lt;p&gt;&#xD;
National Semiconductor T05A&lt;br&gt;&#xD;
Motorola 314D-01""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-T05A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='T05A')

OOMP.parts.append(newPart)