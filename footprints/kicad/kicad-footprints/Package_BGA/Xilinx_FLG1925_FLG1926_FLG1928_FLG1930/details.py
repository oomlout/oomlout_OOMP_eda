###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_FLG1925_FLG1926_FLG1928_FLG1930")

newPart.addTag("kicadDesc", "Virtex-7 BGA, 44x44 grid, 45x45mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=304, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 1924 1 FL1925 FLG1925 FL1926 FLG1926 FL1928 FLG1928 FL1930 FLG1930")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_FLG1925_FLG1926_FLG1928_FLG1930.wrl")

OOMP.parts.append(newPart)