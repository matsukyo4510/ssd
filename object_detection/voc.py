"""
1.訓練・検証の画像とアノテーションのファイルパスリストを作成する関数
"""
import os
def make_filepath_list(rootpath):
    """データパスを格納したリストを作成する。

    Parameters:
        rootpath(str):データフォルダのルートパス
    Returns:
        train_img_list(list):訓練用イメージのパスリスト
        train_anno_list(list):訓練用アノテーションのパスリスト
        val_img_list(list):検証用イメージのパスリスト
        val_anno_list(list):検証用アノテーションのパスリスト
    """

    imgpath_template = os.path.join(rootpath, 'JPEGImages', '%s.jpg')
    