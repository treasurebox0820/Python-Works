import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
from tensorflow.keras.utils import to_categorical
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from PIL import Image
import glob
import os
import random
from tensorflow.keras.preprocessing.image import load_img, img_to_array

import pathlib


def predict_ijin(username_folder):
    """畳み込みニューラルネットワークによる画像認識
    関数内でのフロー
    1. 開発者の顔＋ユーザーの顔で学習
    2. 各偉人を認識用データとして推定
    3. 偉人がユーザーに分類される確率で評価
    4. 最も高い偉人を結果として表示
    """
    # seedの固定のための関数
    def reset_seed(seed=0):
        os.environ['PYTHONHASHSEED'] = '0'
        random.seed(seed)
        np.random.seed(seed)
        tf.random.set_seed(seed)

    # 画像フォルダへのパスを生成
    project_base_path = pathlib.Path().resolve()
    exec_path = 'media'
    target_folder = 'cnn_data'
    p = pathlib.Path('/')
    target_path = p.joinpath(project_base_path, exec_path, target_folder)

    # ユーザー画像のパス
    user_img_folder = 'media\\user'
    user_img_path = p.joinpath(
        project_base_path, user_img_folder, username_folder)

    folder = ['other', 'user']

    cnt_folder = len(folder)
    image_size = 150

    # 画像の読み込み
    X = []
    Y = []
    for index, name in enumerate(folder):
        # userの時だけmedia/user/usernameから引っ張る
        if name == 'user':
            files = glob.glob(str(user_img_path) + '\\*')
        else:
            dir = str(target_path) + '\\' + name
            files = glob.glob(dir + '\\*')

        for i, file in enumerate(files):
            image = Image.open(file)
            image = image.convert('RGB')
            image = image.resize((image_size, image_size))
            data = np.asarray(image)    # arrayに変換
            X.append(data)
            Y.append(index)

    # seedの固定
    reset_seed(0)

    # データセットの作成
    X = np.array(X)
    Y = np.array(Y)

    Y = to_categorical(Y, cnt_folder)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

    # 正規化
    X_train = X_train.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0

    # モデルの定義
    load_model = models.load_model('ijin_model.h5')

    # 学習
    load_model.fit(X_train, Y_train, batch_size=24, epochs=7,
              validation_data=(X_test, Y_test))

    
    # 学習の評価
    score = load_model.evaluate(X_test, Y_test)
    print("\n\n------------------画像認識の結果------------------")
    print('損失=', score[0])
    print('正確さ=', score[1])
    

    # 推定
    # 偉人毎の類似度を格納
    class_dict = {}

    files = glob.glob(str(target_path) + '\\ijin\\*.jpg')
    for file in files:
        # ファイル名の取得
        # ijin_name = os.path.splitext(os.path.basename(file)[0])
        ijin_name = os.path.basename(file).split('.')[0]
        # 画像の読み込み～予測
        img = load_img(file, target_size=(image_size, image_size))
        img = np.expand_dims(img, axis=0)
        img = np.array(img) / 255
        y_pred = load_model.predict(img)

        # ユーザーの確率
        class_dict[ijin_name] = y_pred[0][-1]

    # プレゼン用
    print("\n\n------------似ている度合い(偉人ごと）--------------")
    for k, v in class_dict.items():
        print(f"{k} : {v}")

    # 確率maxの偉人の取得
    user_ijin = max(class_dict.items(), key=lambda x: x[1])
    return user_ijin


if __name__ == "__main__":
    print(predict_ijin('fujioka2'))
