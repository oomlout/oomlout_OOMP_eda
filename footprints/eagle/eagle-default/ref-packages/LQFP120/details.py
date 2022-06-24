###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "LQFP120")
newPart.addTag("oompName", "eagle-default/ref-packages/LQFP120")

newPart.addTag("description", """&lt;b&gt;120-pin Plastic LQFP (FPT-120P-M21)&lt;/b&gt;&lt;p&gt;&#xD;
ds90390-ds07-13722-1e.pdf&lt;br&gt;&#xD;
http://www.fme.gsdc.de""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-LQFP120",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='LQFP120')

OOMP.parts.append(newPart)