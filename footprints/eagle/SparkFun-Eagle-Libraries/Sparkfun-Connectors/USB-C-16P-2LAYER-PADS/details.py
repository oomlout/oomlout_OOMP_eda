###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "USB-C-16P-2LAYER-PADS")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/USB-C-16P-2LAYER-PADS")


newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-USB-C-16P-2LAYER-PADS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='USB-C-16P-2LAYER-PADS')

OOMP.parts.append(newPart)