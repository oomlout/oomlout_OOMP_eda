###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MLP5")
newPart.addTag("oompName", "eagle-default/ref-packages/MLP5")

newPart.addTag("description", """&lt;b&gt;MLP5 Package&lt;/b&gt;&lt;p&gt;&#xD;
Jedec MO-187 Iss A&lt;br&gt;&#xD;
Source : Analog and Discrete Components Databook ST306 April 2001""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MLP5",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MLP5')

OOMP.parts.append(newPart)