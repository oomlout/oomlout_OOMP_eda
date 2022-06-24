###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "RASPBERRY_PI_SHIELD_HOLES")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/RASPBERRY_PI_SHIELD_HOLES")

newPart.addTag("description", """&lt;h3&gt;Surface Mount - 2x20 Header&lt;/h3&gt;

Reversed pinout to match Raspberry Pi male header pinout when coupled.""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-RASPBERRY_PI_SHIELD_HOLES",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='RASPBERRY_PI_SHIELD_HOLES')

OOMP.parts.append(newPart)