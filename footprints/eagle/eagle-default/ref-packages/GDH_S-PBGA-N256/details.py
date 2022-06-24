###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "GDH_S-PBGA-N256")
newPart.addTag("oompName", "eagle-default/ref-packages/GDH_S-PBGA-N256")

newPart.addTag("description", """&lt;b&gt;GDH (S-PBGA-N256)&lt;/b&gt; PLASTIC BALL GRID ARRAY&lt;p&gt;&#xD;
Source: http://focus.ti.com/lit/ds/symlink/tms320c6720.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-GDH_S-PBGA-N256",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='GDH_S-PBGA-N256')

OOMP.parts.append(newPart)