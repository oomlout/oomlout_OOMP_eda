###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "AUDIO-JACK-KIT")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/AUDIO-JACK-KIT")

newPart.addTag("description", """&lt;h3&gt;3.5mm Stereo Audio Jack -Kit Version&lt;/h3&gt;
Reduced openings in tStop, pins spread a tiny bit out to hold part on PCB during assembly
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:5&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=https://www.sparkfun.com/datasheets/Prototyping/Audio-3.5mm.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;Audio_Jack&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-AUDIO-JACK-KIT",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='AUDIO-JACK-KIT')

OOMP.parts.append(newPart)