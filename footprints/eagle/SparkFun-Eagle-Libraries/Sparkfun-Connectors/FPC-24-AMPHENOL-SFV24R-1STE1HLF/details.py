###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "SparkFun-Eagle-Libraries")
newPart.addTag("oompDesc", "Sparkfun-Connectors")
newPart.addTag("oompIndex", "FPC-24-AMPHENOL-SFV24R-1STE1HLF")
newPart.addTag("oompName", "SparkFun-Eagle-Libraries/Sparkfun-Connectors/FPC-24-AMPHENOL-SFV24R-1STE1HLF")

newPart.addTag("description", """&lt;h3&gt;24-Pin FPC/FFC Connector - 0.5mm pitch&lt;/h3&gt;
&lt;p&gt;Digikey: 609-4320-2-ND&lt;/p&gt;
&lt;p&gt;&lt;a href=https://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/10112793.pdf&gt;Datasheet&lt;/a&gt;&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-FPC-24-AMPHENOL-SFV24R-1STE1HLF",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='SparkFun-Eagle-Libraries',oompDesc='Sparkfun-Connectors',oompIndex='FPC-24-AMPHENOL-SFV24R-1STE1HLF')

OOMP.parts.append(newPart)