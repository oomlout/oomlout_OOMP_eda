###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SSOT6")
newPart.addTag("oompName", "eagle-default/ref-packages/SSOT6")

newPart.addTag("description", """&lt;b&gt;SuperSOT-6&lt;/b&gt;&lt;p&gt;&#xD;
Source:  Fairchild Semiconductor International ssot6_dim.pdf&lt;br&gt;&#xD;
  September 1998, Rev. A""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SSOT6",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SSOT6')

OOMP.parts.append(newPart)