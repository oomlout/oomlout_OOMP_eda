###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MICRO3")
newPart.addTag("oompName", "eagle-default/ref-packages/MICRO3")

newPart.addTag("description", """&lt;b&gt;Micro3 TM Package Outline&lt;/b&gt;&lt;p&gt;&#xD;
www.irf.com / irlml5203.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MICRO3",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MICRO3')

OOMP.parts.append(newPart)