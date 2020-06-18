import unittest

import glob
import numpy as np

from cnn_ijin_loadmodel import predict_ijin

class ImageRecognitionTest(unittest.TestCase):
   '''予測の再現性を見る'''
   
   def test_reproducibility_of_predict(self):
       predict1 = predict_ijin()
       predict2 = predict_ijin()
       self.assertEqual(predict1, predict2)


if __name__ == "__main__":
    unittest.main()