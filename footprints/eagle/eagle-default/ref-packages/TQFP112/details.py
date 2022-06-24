###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TQFP112")
newPart.addTag("oompName", "eagle-default/ref-packages/TQFP112")

newPart.addTag("description", """&lt;b&gt;Thin Quad Flat Pack&lt;/b&gt;&lt;p&gt;&#xD;
112-Pin LQFP (Case no. 987) 9S12A256DGV1.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TQFP112",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TQFP112')

OOMP.parts.append(newPart)