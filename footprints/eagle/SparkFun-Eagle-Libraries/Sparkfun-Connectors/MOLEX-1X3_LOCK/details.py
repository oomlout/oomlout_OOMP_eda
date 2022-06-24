###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "MOLEX-1X3_LOCK")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/MOLEX-1X3_LOCK")

newPart.addTag("description", """&lt;h3&gt;PTH - 3 Pin Vertical Molex Polarized Header&lt;/h3&gt;
Pins are offset 0.005&quot; from center to lock pins in place during soldering. 
&lt;p&gt;&lt;b&gt;Datasheet referenced for footprint:&lt;/b&gt;&lt;a href=&quot;http://www.4uconnector.com/online/object/4udrawing/01932.pdf&quot;&gt; 4UCONN part # 01932 &lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:3&lt;/li&gt;
&lt;li&gt;Pin pitch:0.1&quot;&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;CONN_03&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-MOLEX-1X3_LOCK",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='MOLEX-1X3_LOCK')

OOMP.parts.append(newPart)