###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOT323W_PHILIPS")
newPart.addTag("oompName", "eagle-default/ref-packages/SOT323W_PHILIPS")

newPart.addTag("description", """&lt;b&gt;Small Outline Transistor&lt;/b&gt; Wave soldering&lt;p&gt;&#xD;
Philips SC01_Mounting_1996.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOT323W_PHILIPS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOT323W_PHILIPS')

OOMP.parts.append(newPart)