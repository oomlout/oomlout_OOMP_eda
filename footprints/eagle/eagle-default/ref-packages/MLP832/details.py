###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MLP832")
newPart.addTag("oompName", "eagle-default/ref-packages/MLP832")

newPart.addTag("description", """&lt;b&gt;MLP832 Package&lt;/b&gt;&lt;p&gt;&#xD;
Source: www.zetex.com/ .. zxtd1m832.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MLP832",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MLP832')

OOMP.parts.append(newPart)