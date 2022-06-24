###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "1X01_SMALL")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X01_SMALL")

newPart.addTag("description", """&lt;h3&gt;Small PTH Hole&lt;/h3&gt;

&lt;p&gt;Characteristics&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Single through hole&lt;/li&gt;
&lt;li&gt;Diameter: .02&quot;&lt;/li&gt;
&lt;/ul&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-1X01_SMALL",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='1X01_SMALL')

OOMP.parts.append(newPart)