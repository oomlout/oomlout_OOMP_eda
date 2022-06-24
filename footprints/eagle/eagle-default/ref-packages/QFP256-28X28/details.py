###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "QFP256-28X28")
newPart.addTag("oompName", "eagle-default/ref-packages/QFP256-28X28")

newPart.addTag("description", """&lt;b&gt;256-pin QFP&lt;/b&gt; Hitachi Code FP-256G&lt;p&gt;&#xD;
Source: SH7751_R_V3.0.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-QFP256-28X28",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='QFP256-28X28')

OOMP.parts.append(newPart)