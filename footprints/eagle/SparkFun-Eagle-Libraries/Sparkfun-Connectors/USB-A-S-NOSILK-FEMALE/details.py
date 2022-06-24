###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "USB-A-S-NOSILK-FEMALE")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/USB-A-S-NOSILK-FEMALE")

newPart.addTag("description", """&lt;h3&gt;USB Type 'A' Female Connector - SMT No Silk&lt;/h3&gt;
Shield pins may be grounded.
&lt;br&gt; tDocu shows plug end. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:6&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href= https://www.sparkfun.com/datasheets/Prototyping/Connectors/USBFemaleTypeA.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;USB_A&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-USB-A-S-NOSILK-FEMALE",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='USB-A-S-NOSILK-FEMALE')

OOMP.parts.append(newPart)