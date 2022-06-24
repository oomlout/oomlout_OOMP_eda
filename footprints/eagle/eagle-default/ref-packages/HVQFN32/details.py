###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "HVQFN32")
newPart.addTag("oompName", "eagle-default/ref-packages/HVQFN32")

newPart.addTag("description", """&lt;b&gt;HVQFN32&lt;/b&gt; (SOT617-3) 5 x 5 x .85 mm,  Pitch 0.5mm&lt;p&gt;&#xD;
Source: http://www.semiconductors.philips.com/acrobat_download/datasheets/TDA9885_TDA9886_2.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-HVQFN32",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='HVQFN32')

OOMP.parts.append(newPart)