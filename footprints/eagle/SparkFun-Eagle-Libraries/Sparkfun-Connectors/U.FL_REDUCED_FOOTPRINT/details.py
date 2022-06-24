###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "U.FL_REDUCED_FOOTPRINT")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/U.FL_REDUCED_FOOTPRINT")

newPart.addTag("description", """&lt;h3&gt;U.FL SMD Antenna Connector&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;li&gt;Area: 3.0mm x 2.5mm&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://cdn.sparkfun.com/datasheets/Wireless/Antennas/RF-001001.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;U.FL&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-U.FL_REDUCED_FOOTPRINT",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='U.FL_REDUCED_FOOTPRINT')

OOMP.parts.append(newPart)