###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "AUDIO-JACK-3.5MM-SMD")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/AUDIO-JACK-3.5MM-SMD")

newPart.addTag("description", """&lt;h3&gt;3.5mm Stereo Audio Jack - Surface Mount&lt;/h3&gt;
2.5mm Height. 
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:5&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://www.4uconnector.com/online/object/4udrawing/19269.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;Audio_Jack&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-AUDIO-JACK-3.5MM-SMD",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='AUDIO-JACK-3.5MM-SMD')

OOMP.parts.append(newPart)