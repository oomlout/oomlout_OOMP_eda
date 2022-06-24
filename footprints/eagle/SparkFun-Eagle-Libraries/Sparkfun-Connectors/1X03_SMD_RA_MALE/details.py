###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "1X03_SMD_RA_MALE")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X03_SMD_RA_MALE")

newPart.addTag("description", """&lt;h3&gt;SMD- 3 Pin Right Angle Male Headers&lt;/h3&gt;
No silk outline, but tDocu layer shows pin location. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:3&lt;/li&gt;
&lt;li&gt;Pin pitch:0.1&quot;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;CONN_03&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-1X03_SMD_RA_MALE",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='1X03_SMD_RA_MALE')

OOMP.parts.append(newPart)