###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MULTIWAT-SIL13")
newPart.addTag("oompName", "eagle-default/ref-packages/MULTIWAT-SIL13")

newPart.addTag("description", """&lt;b&gt;DBS13P&lt;/b&gt; plastic DIL-bent-SIL power package&lt;p&gt;&#xD;
13 leads (lead length 12 mm) SOT141-6&lt;br&gt;&#xD;
Source: TDA1516BQ_1.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MULTIWAT-SIL13",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MULTIWAT-SIL13')

OOMP.parts.append(newPart)