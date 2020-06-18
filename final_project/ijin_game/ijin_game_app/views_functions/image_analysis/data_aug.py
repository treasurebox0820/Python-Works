from tensorflow.keras.preprocessing import image
import glob
import pathlib
import numpy as np


def augument_data(username_folder):

    # 水増し処理
    data_gen = image.ImageDataGenerator(
        # 水平方向反転
        horizontal_flip=True,
        # 拡大
        zoom_range=0.5,
        # 平行移動
        width_shift_range=0.3,
        height_shift_range=0.3,
        # 回転
        rotation_range=45
    )

    # フォルダの指定
    project_base_path = pathlib.Path().resolve()
    exec_path = 'media'
    target_folder = 'user'
    p = pathlib.Path('/')
    target_path = p.joinpath(project_base_path, exec_path,
                             target_folder, username_folder)

    # ファイルの取得
    files = glob.glob(str(target_path) + '\\*')

    for file in files:
        # ファイルの読み込み, 4次元arrayへの変換
        img = image.load_img(file)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        # 水増し処理(対象のデータ, バッチサイズ, 保存先, 保存時の名前[imgから始まる], 保存形式)
        g = data_gen.flow(x, batch_size=1, save_to_dir=str(
            target_path)+"\\", save_prefix='img', save_format='jpg')

        # 1枚に対し何回拡張するか
        for i in range(4):
            bach = g.next()


if __name__ == "__main__":
    augument_data('nishitani')
