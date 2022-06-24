###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "FPC05040-17204")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/FPC05040-17204")

newPart.addTag("description", """This is a 40-pin FPC connector supplied by Atom. SparkFun SKU is 
CONN-14082""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-FPC05040-17204",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='FPC05040-17204')

OOMP.parts.append(newPart)