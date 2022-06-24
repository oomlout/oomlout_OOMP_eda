###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "SMTSO-256-ET-0.165DIA")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/SMTSO-256-ET-0.165DIA")

newPart.addTag("description", """&lt;h3&gt;SMTSO-256-ET Flush Mount Nut&lt;/h3&gt;
.165 drill
&lt;br&gt;
Fits 4-40 Screws. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 1&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;CONN_01&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-SMTSO-256-ET-0.165DIA",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='SMTSO-256-ET-0.165DIA')

OOMP.parts.append(newPart)