###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SOT536-1")
newPart.addTag("oompName", "eagle-default/ref-packages/SOT536-1")

newPart.addTag("description", """&lt;b&gt;LFBGA96&lt;/b&gt; SOT536-1&lt;p&gt;&#xD;
plastic low profile fine-pitch ball grid array package&lt;br&gt;&#xD;
96 balls; body 13.5 x 5.5 x 1.05 mm&lt;br&gt;&#xD;
SOT536-1.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SOT536-1",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SOT536-1')

OOMP.parts.append(newPart)