###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MSOP10")
newPart.addTag("oompName", "eagle-default/ref-packages/MSOP10")

newPart.addTag("description", """&lt;b&gt;10-Lead Mini Small Outline Package [MSOP]&lt;/b&gt; (RM-10)&lt;p&gt;&#xD;
Source: http://www.analog.com/UploadedFiles/Data_Sheets/35641221898805SSM2167_b.pdf&lt;br&gt;&#xD;
COMPLIANT TO JEDEC STANDARDS MO-187BA""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MSOP10",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MSOP10')

OOMP.parts.append(newPart)