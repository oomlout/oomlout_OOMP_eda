###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOT363_PHILIPS")
newPart.addTag("oompName", "eagle-default/ref-packages/SOT363_PHILIPS")

newPart.addTag("description", """&lt;b&gt;Small Outline Transistor; 6 leads&lt;/b&gt;&lt;p&gt;&#xD;
Philips Semiconductors, SOT363.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOT363_PHILIPS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOT363_PHILIPS')

OOMP.parts.append(newPart)