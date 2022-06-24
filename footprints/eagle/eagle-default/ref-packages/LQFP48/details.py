###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "LQFP48")
newPart.addTag("oompName", "eagle-default/ref-packages/LQFP48")

newPart.addTag("description", """&lt;b&gt;48-pin plastic LQFP (FPT-48P-M26)&lt;/b&gt;&lt;p&gt;&#xD;
www.fma.fujitsu.com/pdf/e713717.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-LQFP48",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='LQFP48')

OOMP.parts.append(newPart)