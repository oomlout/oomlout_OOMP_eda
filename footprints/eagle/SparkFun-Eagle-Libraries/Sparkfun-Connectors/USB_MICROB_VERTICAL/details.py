###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "USB_MICROB_VERTICAL")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/USB_MICROB_VERTICAL")

newPart.addTag("description", """&lt;h3&gt;USB Micro-B Plug Connector&lt;/h3&gt;
Manufacturer part #: ZX80-B-5SA&lt;br&gt;
Manufacturer: Hirose&lt;br&gt;
&lt;p&gt;Specifications:
&lt;ul&gt;&lt;li&gt;Pin count: 5 main, 4 shield&lt;/li&gt;
&lt;p&gt;&lt;a href=https://www.hirose.com/product/en/download_file/key_name/ZX/category/Catalog/doc_file_id/31704/?file_category_id=4&amp;item_id=13&amp;is_series=1&gt;Datasheet referenced for footprint&lt;/a&gt;&lt;/p&gt;
&lt;/ul&gt;&lt;/p&gt;
&lt;p&gt;Example device(s):
&lt;ul&gt;&lt;li&gt;USB_Micro-B&lt;/li&gt;
&lt;/ul&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-USB_MICROB_VERTICAL",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='USB_MICROB_VERTICAL')

OOMP.parts.append(newPart)