###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "MICRO-B-TH")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/MICRO-B-TH")

newPart.addTag("description", """&lt;h3&gt;Micro B USB Plug Assembly - Straight Through-hole&lt;/h3&gt;
&lt;b&gt;**UNPROVEN**&lt;/b&gt;&lt;Br&gt;
See Digikey part #H11497-ND""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-MICRO-B-TH",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='MICRO-B-TH')

OOMP.parts.append(newPart)