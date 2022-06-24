###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "LATCHTERMINAL-5MM-4")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/LATCHTERMINAL-5MM-4")

newPart.addTag("description", """Manufacturer: How Der Electronic Co. 
Part Number: HA-522""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-LATCHTERMINAL-5MM-4",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='LATCHTERMINAL-5MM-4')

OOMP.parts.append(newPart)