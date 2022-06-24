###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "AUDIO_JACK_0.25&quot;_TRS_PTH_RA")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/AUDIO_JACK_0.25&quot;_TRS_PTH_RA")

newPart.addTag("description", """&lt;h3&gt;Right Angle -1/4&quot; Stereo Jack&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 6&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://cdn.sparkfun.com/datasheets/Components/General/JP-611%20DD.jpg&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;AUDIO_JACK_TRS_0.25&quot;_PTH_RA&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-AUDIO_JACK_0.25&quot;_TRS_PTH_RA",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='AUDIO_JACK_0.25&quot;_TRS_PTH_RA')

OOMP.parts.append(newPart)