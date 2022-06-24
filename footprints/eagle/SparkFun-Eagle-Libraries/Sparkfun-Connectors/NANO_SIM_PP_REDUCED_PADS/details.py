###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "NANO_SIM_PP_REDUCED_PADS")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/NANO_SIM_PP_REDUCED_PADS")

newPart.addTag("description", """Part#: ATOM-A03621 or MUP-C7801""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-NANO_SIM_PP_REDUCED_PADS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='NANO_SIM_PP_REDUCED_PADS')

OOMP.parts.append(newPart)