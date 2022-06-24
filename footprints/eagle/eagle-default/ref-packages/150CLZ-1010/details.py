###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "150CLZ-1010")
newPart.addTag("oompName", "eagle-default/ref-packages/150CLZ-1010")

newPart.addTag("description", """&lt;b&gt;Aluminum electrolytic capacitors SMD (Chip)&lt;/b&gt;&lt;p&gt;&#xD;
Long life base plate, very low impedance 150 CLZ&lt;p&gt;&#xD;
http://www.bccomponents.com/""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-150CLZ-1010",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='150CLZ-1010')

OOMP.parts.append(newPart)