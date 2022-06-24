###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MLP322")
newPart.addTag("oompName", "eagle-default/ref-packages/MLP322")

newPart.addTag("description", """&lt;b&gt;MLP322 Package&lt;/b&gt;&lt;p&gt;&#xD;
Source: www.zetex.com/ .. zxtam322.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MLP322",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MLP322')

OOMP.parts.append(newPart)