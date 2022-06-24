###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "POWER-SO10")
newPart.addTag("oompName", "eagle-default/ref-packages/POWER-SO10")

newPart.addTag("description", """&lt;b&gt;Power SO-10&lt;/b&gt;&lt;p&gt;&#xD;
http://eu.st.com/stonline/ 3732.pdf and 5691.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-POWER-SO10",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='POWER-SO10')

OOMP.parts.append(newPart)