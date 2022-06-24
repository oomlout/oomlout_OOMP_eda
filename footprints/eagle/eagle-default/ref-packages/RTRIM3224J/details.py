###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIM3224J")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIM3224J")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; BOURNS&lt;p&gt;&#xD;
Side Adjust""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIM3224J",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIM3224J')

OOMP.parts.append(newPart)