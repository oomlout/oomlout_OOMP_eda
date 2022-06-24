###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "175TMP-0808")
newPart.addTag("oompName", "eagle-default/ref-packages/175TMP-0808")

newPart.addTag("description", """&lt;b&gt;Aluminum electrolytic capacitors&lt;/b&gt;&lt;p&gt;&#xD;
High Temperature solid electrolytic SMD 175 TMP&lt;p&gt;&#xD;
http://www.bccomponents.com/""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-175TMP-0808",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='175TMP-0808')

OOMP.parts.append(newPart)