#ifndef RecoEcal_EgammaCoreTools_Mustache_h
#define RecoEcal_EgammaCoreTools_Mustache_h

#include <vector>
#include "DataFormats/CaloRecHit/interface/CaloCluster.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"



namespace reco {
  namespace MustacheKernel {    
      bool inMustache(const float maxEta, const float maxPhi, 
		      const float ClustE, const float ClusEta, 
		      const float ClusPhi);
      bool inDynamicDPhiWindow(const float seedEta, const float seedPhi,
			       const float ClustE, const float ClusEta,
			       const float clusPhi);
     
      std::vector<double> pMustache_;
      std::string pMustacheLocalFile_;
      void setMustacheParameters (const std::vector<double>& p, const std::string pFile) {pMustache_=p; pMustacheLocalFile_=pFile;}
      std::vector<double> pDynPhiWind_;
      void setDynPhiWindowParameters (const std::vector<double>& p) {pDynPhiWind_=p;}
     
  }

  class Mustache {
    
  public:
    void MustacheID(const CaloClusterPtrVector& clusters, 
		    int & nclusters, float & EoutsideMustache);
    void MustacheID(const std::vector<const CaloCluster*>&, 
		    int & nclusers,
		    float & EoutsideMustache); 
    void MustacheID(const reco::SuperCluster& sc, 
		    int & nclusters, 
		    float & EoutsideMustache);


    void MustacheClust(const std::vector<CaloCluster>& clusters, 
		       std::vector<unsigned int>& insideMust, 
		       std::vector<unsigned int>& outsideMust);
    
    void FillMustacheVar(const std::vector<CaloCluster>& clusters);
    //return Functions for Mustache Variables:
    float MustacheE(){return Energy_In_Mustache_;}
    float MustacheEOut(){return Energy_Outside_Mustache_;}
    float MustacheEtOut(){return Et_Outside_Mustache_;}
    float LowestMustClust(){return LowestClusterEInMustache_;}
    int InsideMust(){return included_;}
    int OutsideMust(){return excluded_;}
  private:
    template<class RandomAccessPtrIterator>
      void MustacheID(const RandomAccessPtrIterator&,
		      const RandomAccessPtrIterator&,
		      int& nclusters,
		      float& EoutsideMustache);
    
    float Energy_In_Mustache_;
    float Energy_Outside_Mustache_;
    float Et_Outside_Mustache_;
    float LowestClusterEInMustache_;
    int excluded_;
    int included_;
  };

  
}

#endif
