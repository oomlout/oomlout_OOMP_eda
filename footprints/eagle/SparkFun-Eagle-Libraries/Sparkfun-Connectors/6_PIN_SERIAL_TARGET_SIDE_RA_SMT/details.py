###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "6_PIN_SERIAL_TARGET_SIDE_RA_SMT")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/6_PIN_SERIAL_TARGET_SIDE_RA_SMT")

newPart.addTag("description", """&lt;h3&gt;6 pin Serial Target - Right Angle  SMT&lt;/h3&gt;
Package for devices meant to mate to an FTDI connector. 
&lt;p&gt; tDocu shows pin location. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:6&lt;/li&gt;
&lt;li&gt;Pin pitch: 0.1&quot;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;6_Pin_Serial_Target&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-6_PIN_SERIAL_TARGET_SIDE_RA_SMT",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='6_PIN_SERIAL_TARGET_SIDE_RA_SMT')

OOMP.parts.append(newPart)