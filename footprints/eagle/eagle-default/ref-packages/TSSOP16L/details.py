###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TSSOP16L")
newPart.addTag("oompName", "eagle-default/ref-packages/TSSOP16L")

newPart.addTag("description", """&lt;b&gt;MOLDED TSSOP&lt;/b&gt; JEDEC, 5 x 4.4 x 9.9 mm Body 16 LD, 0.65mm Pitch&lt;p&gt;&#xD;
Source: http://www.national.com/packaging/mkt/mtc16.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TSSOP16L",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TSSOP16L')

OOMP.parts.append(newPart)