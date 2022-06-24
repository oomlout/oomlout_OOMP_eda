###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "T03B")
newPart.addTag("oompName", "eagle-default/ref-packages/T03B")

newPart.addTag("description", """&lt;b&gt;TO-220&lt;/b&gt; 3 lead&lt;p&gt;&#xD;
National Semiconductor T03A / T03B&lt;br&gt;&#xD;
Motorola 221A-04""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-T03B",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='T03B')

OOMP.parts.append(newPart)