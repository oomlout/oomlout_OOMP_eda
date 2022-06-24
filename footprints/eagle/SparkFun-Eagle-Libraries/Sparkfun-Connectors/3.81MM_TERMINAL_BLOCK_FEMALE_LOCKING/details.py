###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "3.81MM_TERMINAL_BLOCK_FEMALE_LOCKING")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/3.81MM_TERMINAL_BLOCK_FEMALE_LOCKING")

newPart.addTag("description", """&lt;h3&gt;MyDAQ Female Right Angle Terminal Block w/ Locking Footprint&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 40&lt;/li&gt;
&lt;li&gt;Pin pitch:3.18mm&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://www.4uconnector.com/online/object/4udrawing/10458.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;MyDAQ&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-3.81MM_TERMINAL_BLOCK_FEMALE_LOCKING",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='3.81MM_TERMINAL_BLOCK_FEMALE_LOCKING')

OOMP.parts.append(newPart)