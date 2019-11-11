#jython script - run through weka jython tool.
# uses packages (use weka package manager to install):
# jfreechartOffscreenRenderer
# tigerJython
#
# see - BaysianNetwork_Output_results.txt for output
#
# imports
import weka.classifiers.bayes.BayesNet as BayesNet
import weka.classifiers.Evaluation as Evaluation
import weka.core.converters.ConverterUtils.DataSource as DS
import weka.gui.graphvisualizer.GraphVisualizer as GraphVisualizer
import java.util.Random as Random
import javax.swing.JFrame as JFrame
import weka.classifiers.Evaluation as Evaluation
import os

# load data
trainData = DS.read(os.environ.get("MOOC_DATA") + os.sep + "train_balanced.arff") # load full train data set
trainData.setClassIndex(trainData.numAttributes() - 1)
testData = DS.read(os.environ.get("MOOC_DATA") + os.sep + "test_balanced.arff") # load full test data set
testData.setClassIndex(testData.numAttributes() - 1)

#this data is from cluster section, combined into 3 atributes
trainDataCluster = DS.read(os.environ.get("MOOC_DATA") + os.sep + "train_3atribs.arff") # load full train data set
trainDataCluster.setClassIndex(trainDataCluster.numAttributes() - 1)


trainData2 = DS.read(os.environ.get("MOOC_DATA") + os.sep + "Train_top2.arff") # load train data
trainData2.setClassIndex(trainData2.numAttributes() - 1)
testData2 = DS.read(os.environ.get("MOOC_DATA") + os.sep + "test_top2.arff") #load test data
testData2.setClassIndex(testData2.numAttributes() - 1)

trainData5 = DS.read(os.environ.get("MOOC_DATA") + os.sep + "Train_top5.arff") # load train data
trainData5.setClassIndex(trainData5.numAttributes() - 1)
testData5 = DS.read(os.environ.get("MOOC_DATA") + os.sep + "test_top5.arff") #load test data
testData5.setClassIndex(testData5.numAttributes() - 1)

trainData10 = DS.read(os.environ.get("MOOC_DATA") + os.sep + "Train_top10.arff") # load train data
trainData10.setClassIndex(trainData10.numAttributes() - 1)
testData10 = DS.read(os.environ.get("MOOC_DATA") + os.sep + "test_top10.arff") #load test data
testData10.setClassIndex(testData10.numAttributes() - 1)

best = [2,5,10,2305]# 4 sets of data
trainData = [trainData2,trainData5,trainData10,trainData]# create array of data - train
testData = [testData2, testData5, testData10, testData]# create array of data - train
#BN = [ BayesNet() for i in range(0,3)]
#evl = [ Evaluation(trainData[i]) for i in range(0,3)]

#loop through all data sets
for x in range (0,3): # change to (0,4) to run on full balaced data set - very slow
   
    
    #check data is ok
    msg = trainData[x].equalHeadersMsg(testData[x])
    if msg is not None:
        raise Exception("Train/test not compatible:\n" + msg)
        
    #------------------K2 N parents--------------------------------
    print("--------------------------------- Results from dataset of Top " + str(best[x]) + " attributes ------------------------------------------")
    print("class attribute: " + str(trainData[x].classAttribute())) 
    
    for n in range (1,5): #try 1 - 4 parents in k2 
        # configure classifier
        BN = BayesNet()
        BN.setOptions(["-D","-Q", "weka.classifiers.bayes.net.search.local.K2", "--", "-P", str(n)])
        #BN.setOptions(["-D","-Q", "weka.classifiers.bayes.net.search.local.TAN", "--"])
        
        # cross-validate classifier
        #evl = Evaluation(data)
        #evl.crossValidateModel(cls, data, 10, Random(1))
        # build classifier
        #cls.buildClassifier(data)
        BN.buildClassifier(trainData[x])
        print("=== BayesNet K2 on Top " + str(best[x])+ " - " + str(n) + " parents (network) ===")
        print(BN.toString())#print tree in text format
        
        #evalute model (use test data - 20%)
        evl = Evaluation(trainData[x])
        #evl.crossValidateModel(cls, testData, 10, Random(1))#ten fold validation
        evl.evaluateModel(BN, testData[x], None)
        print(evl.toSummaryString("=== BayesNet K2 on Top " + str(best[x])+ " - " + str(n) + " parents (stats) ===", False))
        print(evl.toClassDetailsString("=== BayesNet K2 on Top " + str(best[x])+ " - " + str(n) + " parents (class details) ==="))
        print(evl.toMatrixString("=== BayesNet K2 on Top " + str(best[x])+ " - " + str(n) + " parents (confusion matrix) ==="))
        
        # display tree
        gv = GraphVisualizer()
        gv.readBIF(BN.graph())
        frame = JFrame("BayesNet K2  -  " + str(n) + " parents  -  on Top " + str(best[x]))
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setSize(800, 600)
        frame.getContentPane().add(gv)
        frame.setVisible(True)
            
        # adjust tree layout
        gv.layoutGraph()
    


#------------------Tan-------------------------
    #print("Now run TAN") 
    
    # configure classifier - TAN
    BN = BayesNet()
    BN.setOptions(["-D","-Q", "weka.classifiers.bayes.net.search.local.TAN", "--"])
    
    
    # build classifier
    BN.buildClassifier(trainData[x])
    
    print("=== BayesNet TAN on Top " + str(best[x])+ "  (network) ===")
    print(BN.toString())#print tree in text format
    
    #evalute model (use test data - 20%)
    evl = Evaluation(trainData[x])
    evl.evaluateModel(BN, testData[x], None)
    print(evl.toSummaryString("=== BayesNet TAN on Top " + str(best[x])+ " (stats) ===", False))
    print(evl.toClassDetailsString("=== BayesNet TAN on Top " + str(best[x])+ " (class details) ==="))
    print(evl.toMatrixString("=== BayesNet TAN on Top " + str(best[x])+ "  (confusion matrix) ==="))
    
    # display tree
    gv = GraphVisualizer()
    gv.readBIF(BN.graph())
    frame = JFrame("BayesNet TAN on Top " + str(best[x]))
    frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
    frame.setSize(800, 600)
    frame.getContentPane().add(gv)
    frame.setVisible(True)
        
    # adjust tree layout
    gv.layoutGraph()
    

#------------------hill climb-------------------------
    #print("Now run Hill Climb") 
    #run for 1 - 4 parents
    for i in range (1,5):
        # configure classifier - Hill climber
        BN = BayesNet()
        BN.setOptions(["-D","-Q", "weka.classifiers.bayes.net.search.local.HillClimber", "--", "-P", str(i)])
        
        # build classifier
        BN.buildClassifier(trainData[x])
        print("=== BayesNet HillClimber on Top " + str(best[x])+ " - " + str(i) + " parents (network) ===")
        print(BN.toString())#print tree in text format    
    
        #evalute model (use test data - 20%)
        evl = Evaluation(trainData[x])
        evl.evaluateModel(BN, testData[x], None)
        print(evl.toSummaryString("=== BayesNet HillClimber - " + str(i) + " parents - on Top " + str(best[x])+ " (stats) ===", False))
        print(evl.toClassDetailsString("=== BayesNet HillClimber - " + str(i) + " parents - on Top " + str(best[x])+ " (class details) ==="))
        print(evl.toMatrixString("=== BayesNet HillClimber on Top - " + str(i) + " parents - " + str(best[x])+ "  (confusion matrix) ==="))
        
        # display tree
        gv = GraphVisualizer()
        gv.readBIF(BN.graph())
        frame = JFrame("BayesNet HillClimber - " + str(i) + " parents - on Top " + str(best[x]))
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        frame.setSize(800, 600)
        frame.getContentPane().add(gv)
        frame.setVisible(True)
            
        # adjust tree layout
        gv.layoutGraph()
        
#------------now look at reduced dataset from Tsne 3 dimensions------------------
    
print("run a basian network (k2)on reduced dimentionality data")        
BN = BayesNet()
BN.setOptions(["-D","-Q", "weka.classifiers.bayes.net.search.local.K2", "--", "-P","3"])
#BN.setOptions(["-D","-Q", "weka.classifiers.bayes.net.search.local.TAN", "--"])
        
# cross-validate classifier
#evl = Evaluation(data)
#vl.crossValidateModel(BN, Cluster, 10, Random(1))
# build classifier
#cls.buildClassifier(data)
BN.buildClassifier(trainDataCluster)
#print(BN.toString())#print tree in text format
        
#evalute model (use test data - 20%)
evl = Evaluation(trainDataCluster)
evl.crossValidateModel(BN, trainDataCluster, 10, Random(1))#ten fold validation
#evl.evaluateModel(BN, testData[x], None)
print(evl.toSummaryString("=== BayesNet K2 on Top 3 - (stats) ===", False))
print(evl.toClassDetailsString("=== BayesNet K2 on Top 3  (class details) ==="))
print(evl.toMatrixString("=== BayesNet K2 on Top 3 (confusion matrix) ==="))
        
# display tree
gv = GraphVisualizer()
gv.readBIF(BN.graph())
frame = JFrame("BayesNet K2  Cluster  -  on Top 3" )
frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
frame.setSize(800, 600)
frame.getContentPane().add(gv)
frame.setVisible(True)
            
# adjust tree layout
gv.layoutGraph()
    