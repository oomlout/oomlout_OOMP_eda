###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "QFP44_SOT307-2")
newPart.addTag("oompName", "eagle-default/ref-packages/QFP44_SOT307-2")

newPart.addTag("description", """&lt;b&gt;Plastic Quad Flat Package SOT307-2&lt;/b&gt;&lt;p&gt;&#xD;
44 leads (lead length 1.3 mm); body 10 x 10 x 1.75 mm SOT307-2&lt;p&gt;&#xD;
source: http://www.semiconductors.philips.com/&lt;p&gt;&#xD;
LQFP-MSQFP-QFP-SQFP-TQFP-REFLOW.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-QFP44_SOT307-2",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='QFP44_SOT307-2')

OOMP.parts.append(newPart)