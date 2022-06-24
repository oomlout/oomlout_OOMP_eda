###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "1X01_1MM_NO_SILK")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X01_1MM_NO_SILK")

newPart.addTag("description", """&lt;h3&gt;Plated Through Hole - No Silk Outline&lt;/h3&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:1&lt;/li&gt;
&lt;li&gt;Pin pitch:0.1mm&lt;/li&gt;
&lt;li&gt;Hole Size: .7mm&lt;/li&gt;
&lt;li&gt;Annular Ring: 1.2mm&lt;/li&gt;
&lt;/ul&gt;
&lt;/p&gt;
Made for the small  &lt;a href=&quot;https://www.sparkfun.com/products/18221&quot;&gt; 1mm Pitch Headers&lt;/a&gt;.
&lt;p&gt;
&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-1X01_1MM_NO_SILK",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='1X01_1MM_NO_SILK')

OOMP.parts.append(newPart)