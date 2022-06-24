###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "PGA145S")
newPart.addTag("oompName", "eagle-default/ref-packages/PGA145S")

newPart.addTag("description", """&lt;b&gt;S-PGA-15-145-AZ&lt;/b&gt; SOCKED&lt;p&gt;&#xD;
Emulation Technology, Inc.""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-PGA145S",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='PGA145S')

OOMP.parts.append(newPart)