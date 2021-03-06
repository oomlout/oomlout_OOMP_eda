###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "AAR")
newPart.addTag("oompName", "eagle-default/ref-packages/AAR")

newPart.addTag("description", """&lt;b&gt;DM385_AAR&lt;/b&gt; &lt;font color=&quot;red&quot;&gt;edit this description&lt;/font&gt;&lt;p&gt;&#xD;
Auto generated by &lt;i&gt;make-symbol-device-package-bsdl.ulp Rev. 43&lt;/i&gt;&lt;br&gt;&#xD;
Source: DM385_AAR.bsdl""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-AAR",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='AAR')

OOMP.parts.append(newPart)