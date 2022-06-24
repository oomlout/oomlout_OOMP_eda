###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOT343R")
newPart.addTag("oompName", "eagle-default/ref-packages/SOT343R")

newPart.addTag("description", """&lt;b&gt;Small Outline Transistor; reverse pinning; 4 leads&lt;/b&gt;&lt;p&gt;&#xD;
Philips Semiconductors, SOT343R.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOT343R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOT343R')

OOMP.parts.append(newPart)