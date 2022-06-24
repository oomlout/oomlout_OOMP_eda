###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "BINDING_POST")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/BINDING_POST")

newPart.addTag("description", """&lt;h3&gt;Insulated Binding Post&lt;/h3&gt;
Banana-jack compatible post
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;BINDING_POST&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-BINDING_POST",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='BINDING_POST')

OOMP.parts.append(newPart)