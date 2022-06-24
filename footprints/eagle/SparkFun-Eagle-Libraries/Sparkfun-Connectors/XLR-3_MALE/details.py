###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "XLR-3_MALE")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/XLR-3_MALE")

newPart.addTag("description", """&lt;h3&gt;XLR-3 Connector - Package for the NC3MAAH-1 XLR-3 Connector&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 5&lt;/li&gt;
&lt;li&gt;Area: 1 x .7 in&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://www.neutrik.us/zoolu-website/media/download/1429/Drawing+NC3MAAH-1&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-XLR-3_MALE",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='XLR-3_MALE')

OOMP.parts.append(newPart)