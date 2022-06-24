###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "DB9")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/DB9")

newPart.addTag("description", """&lt;h3&gt;9 Pin Serial Connector - Female PCB Mount Right Angle&lt;/h3&gt;
0.318&quot; style. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:11&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=https://www.sparkfun.com/datasheets/Prototyping/Connectors/DB9-PCB.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;DB9&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-DB9",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='DB9')

OOMP.parts.append(newPart)