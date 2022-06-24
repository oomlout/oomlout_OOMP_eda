###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "DIL28-3-ZIF_SOCKET")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/DIL28-3-ZIF_SOCKET")

newPart.addTag("description", """&lt;h3&gt;ZIF Socket 28-Pin 0.3&quot;&lt;/h3&gt;
tDocu shows location of lever when unlocked. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:28&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;ZIF_SOCKET_28-3&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-DIL28-3-ZIF_SOCKET",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='DIL28-3-ZIF_SOCKET')

OOMP.parts.append(newPart)