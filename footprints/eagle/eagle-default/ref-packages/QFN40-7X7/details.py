###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "QFN40-7X7")
newPart.addTag("oompName", "eagle-default/ref-packages/QFN40-7X7")

newPart.addTag("description", """&lt;b&gt;QFN40 7*7*0.9 0.5 P&lt;/b&gt; CASE 488AG?01 ISSUE O&lt;p&gt;&#xD;
Source: http://www.onsemi.com/pub_link/Collateral/488AG.PDF""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-QFN40-7X7",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='QFN40-7X7')

OOMP.parts.append(newPart)