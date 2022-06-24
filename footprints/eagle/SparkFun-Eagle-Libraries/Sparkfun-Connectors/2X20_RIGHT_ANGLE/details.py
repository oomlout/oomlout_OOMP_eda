###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "2X20_RIGHT_ANGLE")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/2X20_RIGHT_ANGLE")

newPart.addTag("description", """&lt;h3&gt;Plated Through Hole - 2x20 Right Angle Header&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:40&lt;/li&gt;
&lt;li&gt;Pin pitch:0.1&quot;&lt;/li&gt;
&lt;/p&gt;
&lt;p&gt;Shroud Specifications
&lt;ul&gt;
&lt;li&gt;56.08mm x 8.5mm x 6.0mm
&lt;li&gt;
&lt;li&gt;
&lt;/ul&gt;
&lt;/p&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-2X20_RIGHT_ANGLE",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='2X20_RIGHT_ANGLE')

OOMP.parts.append(newPart)