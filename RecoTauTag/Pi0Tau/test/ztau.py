import FWCore.ParameterSet.Config as cms

process = cms.Process("tauAna")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("RecoTauTag.Pi0Tau.tauAna_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/0C4FEB17-9E60-DD11-997C-001617E30D00.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/127D3507-9F60-DD11-8922-000423D174FE.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/3C3B899E-9E60-DD11-A3C3-000423D98A44.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/3C75871C-A760-DD11-831A-000423D98B5C.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/3E8B3096-9E60-DD11-B716-000423D99A8E.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/40DE77DB-9E60-DD11-AF56-000423D9853C.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/580A6E92-9E60-DD11-9C5E-001617DBD332.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/7C908AB7-9E60-DD11-9E28-001617C3B6FE.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/964BA36F-9E60-DD11-B602-0019DB29C614.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/9E76A9C7-9E60-DD11-BFC7-000423D991D4.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/A20C2C88-9E60-DD11-BCDE-000423D98B08.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/AEC2A8D0-9E60-DD11-871C-000423D98FBC.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/B4BF9C15-9F60-DD11-B2C4-001617E30D40.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/BA9DC350-A460-DD11-8E4C-000423D99660.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/C07466E5-9E60-DD11-A9CE-000423D6C8E6.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/C475BC71-9E60-DD11-A819-000423D99658.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/CC661688-9E60-DD11-B956-000423D9853C.root',
    '/store/RelVal/CMSSW_2_1_0/RelValZTT/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V5_v1/0001/E4061194-9E60-DD11-904A-000423D99660.root'
    )
)

process.tauAna.histFileName = 'hist_ztau.root'

process.p = cms.Path(process.tauAna)
