###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TSOP28")
newPart.addTag("oompName", "eagle-default/ref-packages/TSOP28")

newPart.addTag("description", """&lt;b&gt;Thin Small Outline Package Gull Wing&lt;/b&gt;&lt;p&gt;&#xD;
type I, package type TS""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TSOP28",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TSOP28')

OOMP.parts.append(newPart)