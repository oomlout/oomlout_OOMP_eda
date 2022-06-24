###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "SCREENKEY_MATING_CONNECTOR")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/SCREENKEY_MATING_CONNECTOR")

newPart.addTag("description", """&lt;h3&gt;FPC/FFC Locking Connector - SMD&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:14&lt;/li&gt;
&lt;li&gt;Pin pitch: 0.5mm&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=https://www.sparkfun.com/datasheets/Prototyping/Connectors/PRT-09586-e58605370.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;SCREENKEY_CONNECTOR&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-SCREENKEY_MATING_CONNECTOR",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='SCREENKEY_MATING_CONNECTOR')

OOMP.parts.append(newPart)