###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "TP_15TH")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/TP_15TH")

newPart.addTag("description", """&lt;h3&gt;Electrically Conductive Via 0.015&quot; Drill&lt;/h3&gt;
Used as a test point connection for pogo pins or other debugging tools. 
&lt;p&gt;Specifications:
&lt;li&gt;Area:0.015&quot;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;TEST_POINT&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-TP_15TH",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='TP_15TH')

OOMP.parts.append(newPart)