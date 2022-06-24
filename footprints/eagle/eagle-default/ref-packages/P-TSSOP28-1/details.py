###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "P-TSSOP28-1")
newPart.addTag("oompName", "eagle-default/ref-packages/P-TSSOP28-1")

newPart.addTag("description", """Infineon &lt;b&gt;P-TSSOP-28-1&lt;/b&gt;&lt;p&gt;&#xD;
TDA 6060 XS cross-ref_pFET-60v_p_chan.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-P-TSSOP28-1",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='P-TSSOP28-1')

OOMP.parts.append(newPart)