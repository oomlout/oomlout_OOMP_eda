###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SO20_SOT163-1-W")
newPart.addTag("oompName", "eagle-default/ref-packages/SO20_SOT163-1-W")

newPart.addTag("description", """&lt;b&gt;SO20 / SOT163-1 Wave soldering&lt;/b&gt; Philips SC01_Mounting_1996.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SO20_SOT163-1-W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SO20_SOT163-1-W')

OOMP.parts.append(newPart)