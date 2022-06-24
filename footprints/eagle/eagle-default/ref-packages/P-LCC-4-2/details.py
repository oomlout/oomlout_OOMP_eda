###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "P-LCC-4/2")
newPart.addTag("oompName", "eagle-default/ref-packages/P-LCC-4/2")

newPart.addTag("description", """&lt;b&gt;Hyper TOPLED &lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.osram.convergy.de/ ... LOG_LSG T671.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-P-LCC-4/2",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='P-LCC-4/2')

OOMP.parts.append(newPart)