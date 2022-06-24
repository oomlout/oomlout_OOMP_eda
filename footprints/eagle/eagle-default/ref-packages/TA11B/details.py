###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TA11B")
newPart.addTag("oompName", "eagle-default/ref-packages/TA11B")

newPart.addTag("description", """&lt;b&gt;TO-220&lt;/b&gt; 11 lead&lt;p&gt;&#xD;
National Semiconductor TA11B""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TA11B",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TA11B')

OOMP.parts.append(newPart)