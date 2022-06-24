###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "EDISON_DAUGHTER")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/EDISON_DAUGHTER")

newPart.addTag("description", """&lt;h3&gt;Hirose DF30C-70DP-0.4V(51) Receiver Footprint w/ Edison Outline&lt;/h3&gt;
Package can be used as basic guideline for creating Edison-mating daughter boards.
&lt;br&gt;Includes keepout area for antenna. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:70&lt;/li&gt;
&lt;li&gt;Pin pitch: 0.4mm&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://media.digikey.com/pdf/Data%20Sheets/Hirose%20PDFs/DF40C-70DP-0.4V(51).pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;EDISON_FULL_CONNECTOR&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-EDISON_DAUGHTER",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='EDISON_DAUGHTER')

OOMP.parts.append(newPart)