###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIM3304W")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIM3304W")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; BOURNS&lt;p&gt;&#xD;
0,1W 25%""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIM3304W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIM3304W')

OOMP.parts.append(newPart)