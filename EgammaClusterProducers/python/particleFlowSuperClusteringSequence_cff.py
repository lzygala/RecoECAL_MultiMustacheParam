import FWCore.ParameterSet.Config as cms

#------------------
#Hybrid clustering:
#------------------
# Producer for Box Particle Flow Super Clusters
from RecoEcal.EgammaClusterProducers.particleFlowSuperClusterECAL_cfi import *
# Producer for energy corrections
#from RecoEcal.EgammaClusterProducers.correctedDynamicHybridSuperClusters_cfi import *
# PFECAL super clusters, either hybrid-clustering clone (Box) or mustache.

particleFlowSuperClusterECALMustacheNewParams = particleFlowSuperClusterECAL.clone()
particleFlowSuperClusterECALMustacheNewParams.PFSuperClusterCollectionBarrel = cms.string("particleFlowSuperClusterECALBarrelMustacheNewParams")
particleFlowSuperClusterECALMustacheNewParams.PFSuperClusterCollectionEndcapWithPreshower = cms.string("particleFlowSuperClusterECALEndcapWithPreshowerMustacheNewParams")
particleFlowSuperClusterECALMustacheNewParams.PFSuperClusterCollectionEndcap = cms.string("particleFlowSuperClusterECALEndcapMustacheNewParams")
particleFlowSuperClusterECALMustacheNewParams.PFBasicClusterCollectionBarrel = cms.string("particleFlowBasicClusterECALBarrelMustacheNewParams")
particleFlowSuperClusterECALMustacheNewParams.PFBasicClusterCollectionEndcap = cms.string("particleFlowBasicClusterECALEndcapMustacheNewParams")
particleFlowSuperClusterECALMustacheNewParams.PFBasicClusterCollectionPreshower = cms.string("particleFlowBasicClusterECALPreshowerMustacheNewParams")
particleFlowSuperClusterECALMustacheNewParams.p00 = cms.double(-0.107537)
particleFlowSuperClusterECALMustacheNewParams.p01 = cms.double(0.590969)
particleFlowSuperClusterECALMustacheNewParams.p02 = cms.double(-0.076494)
particleFlowSuperClusterECALMustacheNewParams.p10 = cms.double(-0.0268843)
particleFlowSuperClusterECALMustacheNewParams.p11 = cms.double(0.147742)
particleFlowSuperClusterECALMustacheNewParams.p12 = cms.double(-0.0191235)
particleFlowSuperClusterECALMustacheNewParams.w00 = cms.double(-0.00740552)
particleFlowSuperClusterECALMustacheNewParams.w01 = cms.double(-0.0034151)
particleFlowSuperClusterECALMustacheNewParams.w10 = cms.double(0.00104861)
particleFlowSuperClusterECALMustacheNewParams.w11 = cms.double(-0.00493385)
#particleFlowSuperClusterECALMustacheNewParams.yoffsetEB = cms.double(0.0254118)
#particleFlowSuperClusterECALMustacheNewParams.scaleEB = cms.double(1.06851)
##particleFlowSuperClusterECALMustacheNewParams.xoffsetEB = cms.double(-0.171274)
#particleFlowSuperClusterECALMustacheNewParams.widthEB = cms.double(0.44781)
#particleFlowSuperClusterECALMustacheNewParams.yoffsetEE_0 = cms.double(0.0495085)
#particleFlowSuperClusterECALMustacheNewParams.scaleEE_0 = cms.double(1.02638)
#particleFlowSuperClusterECALMustacheNewParams.xoffsetEE_0 = cms.double(-0.203591)
#particleFlowSuperClusterECALMustacheNewParams.widthEE_0 = cms.double(0.434453)
#particleFlowSuperClusterECALMustacheNewParams.yoffsetEE_1 = cms.double(0.0482797)
#particleFlowSuperClusterECALMustacheNewParams.scaleEE_1 = cms.double(2.71995)
##particleFlowSuperClusterECALMustacheNewParams.xoffsetEE_1 = cms.double(-1.01813)
#particleFlowSuperClusterECALMustacheNewParams.widthEE_1 = cms.double(0.516745)
#particleFlowSuperClusterECALMustacheNewParams.yoffsetEE_2 = cms.double(-0.47284)
#particleFlowSuperClusterECALMustacheNewParams.scaleEE_2 = cms.double(10.8097)
#particleFlowSuperClusterECALMustacheNewParams.xoffsetEE_2 = cms.double(-4.75781)
#particleFlowSuperClusterECALMustacheNewParams.widthEE_2 = cms.double(2.00665)

#Optimized PFRHT optimized mustache parameters
particleFlowSuperClusterECALMustacheNewParams.w00 = cms.double(-0.00629374)
particleFlowSuperClusterECALMustacheNewParams.w01 = cms.double(-0.0034151)
particleFlowSuperClusterECALMustacheNewParams.w10 = cms.double(0.00104861)
particleFlowSuperClusterECALMustacheNewParams.w11 = cms.double(-0.00493385)
particleFlowSuperClusterECALMustacheNewParams.yoffsetEB = cms.double(0.0280506)
particleFlowSuperClusterECALMustacheNewParams.scaleEB = cms.double(1.06851)
particleFlowSuperClusterECALMustacheNewParams.xoffsetEB = cms.double(-0.171274)
particleFlowSuperClusterECALMustacheNewParams.widthEB = cms.double(0.44781)
particleFlowSuperClusterECALMustacheNewParams.yoffsetEE_0 = cms.double(0.0495085)
particleFlowSuperClusterECALMustacheNewParams.scaleEE_0 = cms.double(1.02638)
particleFlowSuperClusterECALMustacheNewParams.xoffsetEE_0 = cms.double(-0.203591)
particleFlowSuperClusterECALMustacheNewParams.widthEE_0 = cms.double(0.434453)
particleFlowSuperClusterECALMustacheNewParams.yoffsetEE_1 = cms.double(0.0482797)
particleFlowSuperClusterECALMustacheNewParams.scaleEE_1 = cms.double(2.71995)
particleFlowSuperClusterECALMustacheNewParams.xoffsetEE_1 = cms.double(-1.01813)
particleFlowSuperClusterECALMustacheNewParams.widthEE_1 = cms.double(0.516745)
particleFlowSuperClusterECALMustacheNewParams.yoffsetEE_2 = cms.double(-0.47284)
particleFlowSuperClusterECALMustacheNewParams.scaleEE_2 = cms.double(10.8097)
particleFlowSuperClusterECALMustacheNewParams.xoffsetEE_2 = cms.double(-4.75781)
particleFlowSuperClusterECALMustacheNewParams.widthEE_2 = cms.double(2.00665)

particleFlowSuperClusterECALMustacheNewParams.mustacheParametersLocalFileInPath = cms.FileInPath("RecoEcal/EgammaClusterProducers/data/mustacheLocalParameters_optimized.txt")

particleFlowSuperClusteringTask = cms.Task(particleFlowSuperClusterECAL,particleFlowSuperClusterECALMustacheNewParams)
particleFlowSuperClusteringSequence = cms.Sequence(particleFlowSuperClusteringTask)

particleFlowSuperClusterHGCal = particleFlowSuperClusterECAL.clone()
from Configuration.Eras.Modifier_phase2_hgcal_cff import phase2_hgcal
phase2_hgcal.toModify(
    particleFlowSuperClusterHGCal,
    PFClusters = cms.InputTag('particleFlowClusterHGCal'),
    useRegression = cms.bool(False), #no HGCal regression yet
    use_preshower = cms.bool(False),
    PFBasicClusterCollectionEndcap = cms.string(""),
    PFSuperClusterCollectionEndcap = cms.string(""),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string(""),
    thresh_PFClusterEndcap = cms.double(1.5e-1), # 150 MeV threshold
    dropUnseedable = cms.bool(True),
)

particleFlowSuperClusterHGCalFromMultiCl = particleFlowSuperClusterHGCal.clone()
phase2_hgcal.toModify(
    particleFlowSuperClusterHGCalFromMultiCl,
    PFClusters = cms.InputTag('particleFlowClusterHGCalFromMultiCl')
)
_phase2_hgcal_particleFlowSuperClusteringSequence = particleFlowSuperClusteringSequence.copy()
_phase2_hgcal_particleFlowSuperClusteringSequence += particleFlowSuperClusterHGCal
_phase2_hgcal_particleFlowSuperClusteringSequence += particleFlowSuperClusterHGCalFromMultiCl

phase2_hgcal.toReplaceWith( particleFlowSuperClusteringSequence, _phase2_hgcal_particleFlowSuperClusteringSequence )

