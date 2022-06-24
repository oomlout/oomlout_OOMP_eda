###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TOP3BHS")
newPart.addTag("oompName", "eagle-default/ref-packages/TOP3BHS")

newPart.addTag("description", """&lt;b&gt;Molded Package&lt;/b&gt;&lt;p&gt;&#xD;
grid 5.45 mm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TOP3BHS",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TOP3BHS')

OOMP.parts.append(newPart)