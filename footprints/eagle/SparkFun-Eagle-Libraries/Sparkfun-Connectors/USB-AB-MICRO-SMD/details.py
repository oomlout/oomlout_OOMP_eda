###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "USB-AB-MICRO-SMD")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/USB-AB-MICRO-SMD")

newPart.addTag("description", """&lt;h3&gt;USB Type AB - SMT&lt;/h3&gt;
&lt;br&gt; Basic silk outline&lt;/br&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count:5 main, 3 shield&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;&lt;b&gt;Datasheet referenced for footprint: http://www.morethanall.com//upload/products_pdf/87340574052ba5151280ca.pdf&lt;/b&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;USB AB&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-USB-AB-MICRO-SMD",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='USB-AB-MICRO-SMD')

OOMP.parts.append(newPart)