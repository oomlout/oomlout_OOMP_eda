###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "POWER_JACK_PTH_BREAD")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/POWER_JACK_PTH_BREAD")

newPart.addTag("description", """&lt;h3&gt;DC Barrel Power Jack/Connector Breadboard Compatible&lt;/h3&gt;
Breadboard-friendly pins. 
5.5mm jack, 2.1mm center pole diameter
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 3&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://cdn.sparkfun.com/datasheets/Prototyping/18742.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;POWER_JACK&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-POWER_JACK_PTH_BREAD",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='POWER_JACK_PTH_BREAD')

OOMP.parts.append(newPart)