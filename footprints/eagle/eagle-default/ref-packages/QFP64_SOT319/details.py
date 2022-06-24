###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "QFP64_SOT319")
newPart.addTag("oompName", "eagle-default/ref-packages/QFP64_SOT319")

newPart.addTag("description", """&lt;b&gt;Plastic Quad Flat Package SOT319-1/-2/-5&lt;/b&gt; 64 leads &lt;p&gt;&#xD;
source: http://www.semiconductors.philips.com/&lt;p&gt;&#xD;
LQFP-MSQFP-QFP-SQFP-TQFP-REFLOW.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-QFP64_SOT319",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='QFP64_SOT319')

OOMP.parts.append(newPart)