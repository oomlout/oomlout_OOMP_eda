###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "STEREOJACK2.5MM_SPECIAL_POGOPINS")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/STEREOJACK2.5MM_SPECIAL_POGOPINS")

newPart.addTag("description", """&lt;h3&gt;2.5mm Stereo Audio Jack - PTH Pogo Pin Compatible&lt;/h3&gt;
Long pads to enable testing with pogo pins.
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:4&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href=http://www.4uconnector.com/online/object/4udrawing/19726.pdf&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;Audio_Jack_2.5MM&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-STEREOJACK2.5MM_SPECIAL_POGOPINS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='STEREOJACK2.5MM_SPECIAL_POGOPINS')

OOMP.parts.append(newPart)