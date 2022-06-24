###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "QFP100_SOT317-SOT382-2")
newPart.addTag("oompName", "eagle-default/ref-packages/QFP100_SOT317-SOT382-2")

newPart.addTag("description", """&lt;b&gt;Plastic Quad Flat Package SOT317-1/-2/-3 SOT382-2&lt;/b&gt; 100 leads &lt;p&gt;&#xD;
source: http://www.semiconductors.philips.com/&lt;p&gt;&#xD;
LQFP-MSQFP-QFP-SQFP-TQFP-REFLOW.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-QFP100_SOT317-SOT382-2",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='QFP100_SOT317-SOT382-2')

OOMP.parts.append(newPart)