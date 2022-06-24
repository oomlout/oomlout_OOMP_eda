###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "DB9_MALE")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/DB9_MALE")

newPart.addTag("description", """&lt;h3&gt;9 Pin Serial Connector - Male PCB Mount Right Angle&lt;/h3&gt;
0.318&quot; style. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:11&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://www.4uconnector.com/online/object/4udrawing/15944.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;DB9&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-DB9_MALE",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='DB9_MALE')

OOMP.parts.append(newPart)