###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "JST-5-PTH-VERT")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/JST-5-PTH-VERT")

newPart.addTag("description", """&lt;h3&gt;JST 5 Pin Vertical Plated Through Hole&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 5&lt;/li&gt;
&lt;li&gt;Pin pitch: 2mm&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;CONN_05&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-JST-5-PTH-VERT",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='JST-5-PTH-VERT')

OOMP.parts.append(newPart)