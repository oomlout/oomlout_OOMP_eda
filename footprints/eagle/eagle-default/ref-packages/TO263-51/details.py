###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TO263-51")
newPart.addTag("oompName", "eagle-default/ref-packages/TO263-51")

newPart.addTag("description", """&lt;b&gt;Transistor Outline Package&lt;/b&gt;&lt;p&gt;&#xD;
P-TO263-5-1 SIEMENS TLE4270""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TO263-51",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TO263-51')

OOMP.parts.append(newPart)