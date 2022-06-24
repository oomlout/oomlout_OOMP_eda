###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "PAD.03X.03")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/PAD.03X.03")

newPart.addTag("description", """&lt;h3&gt;Electrically Conductive Pad 0.03&quot; Circle&lt;/h3&gt;
Used as a test point connection for pogo pins or other debugging tools. 
&lt;p&gt;Specifications:
&lt;li&gt;Area: 0.03&quot; x 0.03&quot;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;TEST_POINT&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-PAD.03X.03",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='PAD.03X.03')

OOMP.parts.append(newPart)