###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "R-PDSO-G20")
newPart.addTag("oompName", "eagle-default/ref-packages/R-PDSO-G20")

newPart.addTag("description", """&lt;b&gt;PLASTIC SMALL-OUTLINE PACKAGE SO 20&lt;/b&gt; JEDEC MO-153&lt;p&gt;&#xD;
Source: www.ti.com/.. slvs087l.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-R-PDSO-G20",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='R-PDSO-G20')

OOMP.parts.append(newPart)