from SpencerLimitEquilibrium.CharacteristicsOfSlopeGeometryAttribute import CharacteristicsOfSlopeGeometryAttribute
from SpencerLimitEquilibrium.NumberOfSlices import NumberOfSlices
from SpencerLimitEquilibrium.CharacteristicsOfSlopeGeometry import CharacteristicsOfSlopeGeometry
from SpencerLimitEquilibrium.SlipSurface import SlipSurface
from SpencerLimitEquilibrium.PropertiesMaterials import PropertiesMaterials
from SpencerLimitEquilibrium.Forces import Forces
from SpencerLimitEquilibrium.WetSpecificWeight import WetSpecificWeight
from SpencerLimitEquilibrium.ImportantCoordinatesCircle import ImportantCoordinatesCircle
from SpencerLimitEquilibrium.WidthSlices import WidthSlices




while True:
    try:
        csga = CharacteristicsOfSlopeGeometryAttribute(12,10,4)
        csg = CharacteristicsOfSlopeGeometry(csga)
        nofs = NumberOfSlices(1,2,3)
        ss = SlipSurface(20,20)
        pm = PropertiesMaterials(1,2,3,4,5,6)
        wsw = WetSpecificWeight(pm)
        fcs = Forces(wsw,20)
        icc = ImportantCoordinatesCircle(ss,csg)
        ws = WidthSlices(icc,nofs,csg)

        print(csg.sideSmall)
        print(csg.sideBig)
        print(nofs.numberOfSlices)
        print(ss.radius)
        print(pm.gammaWatter)
        print(pm.gs)
        print(fcs.forceVertical)
        print(icc.intersectionEmbankmentAndSlipSurface)

        break
    except:
        pass



