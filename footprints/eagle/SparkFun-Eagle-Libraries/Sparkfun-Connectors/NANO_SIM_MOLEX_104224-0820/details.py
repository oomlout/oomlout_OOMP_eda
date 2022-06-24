###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "NANO_SIM_MOLEX_104224-0820")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/NANO_SIM_MOLEX_104224-0820")

newPart.addTag("description", """&lt;h3&gt;Molex Nano-SIM Holder &amp;ndash; 1042240820&lt;/h3&gt;
&lt;a href=https://www.molex.com/pdm_docs/sd/1042240820_sd.pdf&gt;Datasheet&lt;/a&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-NANO_SIM_MOLEX_104224-0820",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='NANO_SIM_MOLEX_104224-0820')

OOMP.parts.append(newPart)