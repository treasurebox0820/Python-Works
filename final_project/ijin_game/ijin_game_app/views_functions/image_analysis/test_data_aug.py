import unittest

import glob, pathlib
import numpy as np

from data_aug import augument_data

class DataAugmentationTest(unittest.TestCase):
   '''データの拡張を見る'''
   # userの画像データ増えるか
   def test_data_augmentation(self):
       # フォルダの指定
       project_base_path = pathlib.Path().resolve()
       user_img_folder = 'media\\user'
       p = pathlib.Path('/')
       user_img_path = p.joinpath(project_base_path, user_img_folder)
       
       files = glob.glob(str(user_img_path) + '\\*')
       augument_data()
       aug_files = glob.glob(str(user_img_path) + '\\*')
       self.assertGreater(len(aug_files), len(files))

if __name__ == "__main__":
    unittest.main()