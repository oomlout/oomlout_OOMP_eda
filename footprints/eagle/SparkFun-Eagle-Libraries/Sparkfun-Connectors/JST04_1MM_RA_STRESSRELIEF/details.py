###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "JST04_1MM_RA_STRESSRELIEF")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/JST04_1MM_RA_STRESSRELIEF")

newPart.addTag("description", """Qwiic connector with milled cutout. Sliding the cable into this slot prevents the cable from coming unplugged.""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-JST04_1MM_RA_STRESSRELIEF",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='JST04_1MM_RA_STRESSRELIEF')

OOMP.parts.append(newPart)