# 開発用リポジトリ : ijingame
# アプリ名：Youは何した偉人さん？
# チーム名：さわやか三期 ～♪さん　さん　さん　太陽の～ひかり～

## ====================
## リポジトリ構成
## ====================

## 1. ijin_game
- 「Youは何した偉人さん？」のDjangoアプリケーションを管理する。
- 各担当が作成したUI、Djangoアプリケーション、画像解析機能、構文解析機能を当該フォルダに格納する。
- 最終的に動作するアプリケーションは当該フォルダを実行したものになる。

## 2. UI
- UIやデザインに関するソースコードを管理する。
- Djangoに組み込む前にレイアウトを確認したりする場合、単独で表示可能なHTML・CSS等をここに格納する。

## 3. web
- webに関するソースコードを管理する。
- Djangoの実験的な実装やデータ投入用のSQL文等をここに格納する。
- ただし、webに関するソースコードは基本的に「1. ijin_game」で管理する。

## 4. 画像解析
- 画像解析に関するスクリプトを管理する。
- Djangoに組み込む前にチューニングしたり、単独で動作させたい実験的なスクリプトをここに格納する。
- CNNに関するpythonスクリプト等

## 5. 構文解析
- 構文解析に関するスクリプトを管理する。
- Djangoに組み込む前にチューニングしたり、単独で動作させたい実験的なスクリプトをここに格納する。
- TF-IDFに関するpythonスクリプト等

## 6. 前処理
- 前処理に関するスクリプトを管理する。
- 画像撮影や画像加工に使用するスクリプトをここに格納する。
- openCVに関するPythonスクリプト等

## ====================
## アプリ実行手順
## ====================

## 前提
---
1. pipインストールによる開発環境構築が完了していること。  
[開発環境構築手順書(Google Drive)](https://drive.google.com/open?id=187sA82L1K-aXJ8VeH7tyElQWoBY1rpth)

2. 当該リポジトリをローカルPCにクローンしていること。

3. データベース作成が完了していること。  
[データベース環境構築手順書](https://drive.google.com/open?id=1Ocj4rTpTLAOz2Vmx7tB79YnerCHTiYKB)

4. データベースの再作成
    - テーブルを作成してしまっている場合、テーブルデータが消えても大丈夫ならデータベースを一度削除して再生成する。  

    - **データベースの削除→作成手順**
        1. mysqlにrootユーザでログイン  

            ` mysql -u root -p `

        2. データベースを削除  

            ` drop database ijin_db; `
        
        3. データベースを作成  

            ` create database ijin_db default character set utf8; `


## アプリ実行手順
---
1. 当該アプリケーション開発用の仮想環境をacitivateする。

2. コンソール上でカレントディレクトリを「ijin_game」に移動する。

3. 【実施不要】モデルを反映する。  
    最初にマイグレーションファイルの作成を行う。  
    リポジトリにマイグレーションファイル(0001_initial.py)が上がっているので、それをマイグレートすればよい。  

    ` python manage.py makemigrations `

4. 【実施不要】マイグレーションファイルのSQL実行イメージを確認する。  
    Djangoがテーブル生成を行うSQLを確認したい場合のみ実行する。このコマンドではまだテーブルは生成されない。  

    ` python manage.py sqlmigrate ijin_game_app 0001_initial `

5. マイグレート実行してデータベースにテーブルを生成する。  

    ` python manage.py migrate `

6. Djangoのスーパーユーザを作成する。  
    Django管理サイトにアクセスできるスーパーユーザを作成する。  
    スーパーユーザを作成すると、Django管理画面でテーブルにデータ投入したり修正したりできる。

    ```
    usernameとpassは任意だが管理者とわかるようにする。
    python manage.py createsuperuser
    username:
    admin
    pass:
    admin
    OK?(passwordとか短すぎるけどいいの？って聞かれるのでOK)
    y
    ```

7. 機械学習用のデータを以下のとおり配置する。
    - 画像解析用データ  
        以下の場所にある「cnn_data」フォルダを「ijin_game\media」配下に配置する。  
        https://drive.google.com/open?id=1vGPox7w1FDzRgQx_bEiYe7tpz_ePa6kN

    - 構文解析用データ
        以下の場所にある「saved_model」フォルダを  
        「ijin_game\ijin_game_api\views_functions\syntactic_analysis」配下に配置する。  
        ★「ijin_game\ijin_game_api」である点に注意する。「ijin_game\ijin_game_app」ではない。  
        https://drive.google.com/open?id=1Vm4HvbS3O77_lO8ZdIGWJdnQEYXQ1067

8. Djnagoを起動する。  
    ` python manage.py runserver `

9. Django管理画面にアクセスする。  
    http://localhost:8000/admin/

10. 作成したスーパーユーザのIDとpassを入力して管理画面にログインする。

11. 必要に応じてDB初期データを投入する。

12. ログアウトする。  
    ※ログアウトしないとadminユーザでログインしたままになり、  
    Djangoでの偉人ゲーム操作時に想定しないユーザ(adminユーザ)で操作することになる。

13. ブラウザでトップページにアクセスする。  
    http://localhost:8000/

14. 「Youは何した偉人さん？」のトップページが表示されることを確認する。

15. 「Youは何した偉人さん？」が一通り遊べることを確認する。