###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "MICRO-B-SMT")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/MICRO-B-SMT")

newPart.addTag("description", """&lt;h3&gt;USB Micro-B Plug Connector&lt;/h3&gt;
Manufacturer part #: ZX80-B-5SA&lt;br&gt;
Manufacturer: Hirose&lt;br&gt;&lt;br&gt;
&lt;b&gt;***Unproven***&lt;/b&gt; (Passed 1:1 printout test though!)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-MICRO-B-SMT",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='MICRO-B-SMT')

OOMP.parts.append(newPart)