###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "RASPBERRY_PI_HAT_40_PIN_SMD_STACKABLE")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/RASPBERRY_PI_HAT_40_PIN_SMD_STACKABLE")

newPart.addTag("description", """&lt;h3&gt;Plated Through Hole - 2x20&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:40&lt;/li&gt;
&lt;li&gt;Pin pitch:0.1&quot;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;CONN_20x2&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-RASPBERRY_PI_HAT_40_PIN_SMD_STACKABLE",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='RASPBERRY_PI_HAT_40_PIN_SMD_STACKABLE')

OOMP.parts.append(newPart)