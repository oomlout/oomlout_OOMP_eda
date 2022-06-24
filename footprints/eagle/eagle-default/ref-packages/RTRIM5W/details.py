###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIM5W")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIM5W")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; Spectrol&lt;p&gt;&#xD;
abgedichtet nach &lt;b&gt;IP67&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIM5W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIM5W')

OOMP.parts.append(newPart)