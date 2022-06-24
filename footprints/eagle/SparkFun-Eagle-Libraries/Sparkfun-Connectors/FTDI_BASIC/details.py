###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "FTDI_BASIC")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/FTDI_BASIC")

newPart.addTag("description", """&lt;h3&gt;FTDI Basic &lt;/h3&gt;
Includes tDocu labels for end pins that match the FTDI Basic connection.
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 6&lt;/li&gt;
&lt;li&gt;Pin pitch: 0.1&quot;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;6_Pin_Serial_Cable&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-FTDI_BASIC",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='FTDI_BASIC')

OOMP.parts.append(newPart)