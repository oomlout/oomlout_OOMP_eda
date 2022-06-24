###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "AUDIO_JACK_3.5MM_TRRS_SMD_RA")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/AUDIO_JACK_3.5MM_TRRS_SMD_RA")

newPart.addTag("description", """&lt;h3&gt;TRRS 3.5MM Right Angle Stereo Jack - SMT&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 4&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://cdn.sparkfun.com/datasheets/Prototyping/20153.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;AUDIO_JACK_TRRS&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-AUDIO_JACK_3.5MM_TRRS_SMD_RA",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='AUDIO_JACK_3.5MM_TRRS_SMD_RA')

OOMP.parts.append(newPart)