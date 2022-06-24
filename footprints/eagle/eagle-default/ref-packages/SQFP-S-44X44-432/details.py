###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SQFP-S-44X44-432")
newPart.addTag("oompName", "eagle-default/ref-packages/SQFP-S-44X44-432")

newPart.addTag("description", """&lt;b&gt;QFP432&lt;/b&gt;&lt;p&gt;&#xD;
shrink quad flat pack, square""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SQFP-S-44X44-432",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SQFP-S-44X44-432')

OOMP.parts.append(newPart)