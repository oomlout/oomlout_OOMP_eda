###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TA15A")
newPart.addTag("oompName", "eagle-default/ref-packages/TA15A")

newPart.addTag("description", """&lt;b&gt;TO-220&lt;/b&gt; 15 lead&lt;p&gt;&#xD;
National Semiconductor TA15A""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TA15A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TA15A')

OOMP.parts.append(newPart)