###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOT457W_PHILIPS")
newPart.addTag("oompName", "eagle-default/ref-packages/SOT457W_PHILIPS")

newPart.addTag("description", """&lt;b&gt;Small Outline Transistor; 6 leads&lt;/b&gt;&lt;p&gt;&#xD;
SOT457 (SC-74) FOOTPRINT (WAFE SOLDERING)&lt;p&gt;&#xD;
Philips Semiconductors,  sot457-(sc-74)-reflow-wave.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOT457W_PHILIPS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOT457W_PHILIPS')

OOMP.parts.append(newPart)