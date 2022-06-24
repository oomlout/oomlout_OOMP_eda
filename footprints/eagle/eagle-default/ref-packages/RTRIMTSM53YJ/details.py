###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIMTSM53YJ")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIMTSM53YJ")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; VISHAY&lt;p&gt;&#xD;
abgedichtet nach &lt;b&gt;IP67&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIMTSM53YJ",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIMTSM53YJ')

OOMP.parts.append(newPart)