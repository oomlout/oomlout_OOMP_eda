###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "EB-85A")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/EB-85A")

newPart.addTag("description", """&lt;h3&gt;EB-85A Connector&lt;/h3&gt;
Horizontal surface mount connector for the EB-85A/FV-M8 GPS receiver.
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 10&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=https://www.sparkfun.com/datasheets/GPS/EB-85A-Connector.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;EB-85A&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-EB-85A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='EB-85A')

OOMP.parts.append(newPart)