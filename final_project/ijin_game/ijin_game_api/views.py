from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .views_functions.syntactic_analysis import NLP_main


class SyntacticAnalysis(APIView):
    """構文解析API

    構文解析処理を呼び出すAPI

    Args:
        APIView (APIView): モデルに紐づかないクラスベースビュー
    """

    # def get(self, request, format=None):
    #     # TODO request.data等のメソッドを使い、ijin_nameとtextを受け取る
    #     ijin_name = "夏目漱石"
    #     input_text = "夏目漱石は胃潰瘍だった。代表作は『吾輩は猫である』『坊っちゃん』『こゝろ』など。明治の文豪として日本の千円紙幣の肖像にもなり、講演録「私の個人主義」も知られている。漱石の私邸に門下生が集った会は木曜会と呼ばれた。"
        
    #     nlp_result_dict = {
    #         "score": NLP_main.main(ijin_name, input_text)
    #     }

    #     return Response(nlp_result_dict)


    def post(self, request, format=None):

        dict_ = request.data
        # dict_はAPIで取得したデータのため、JSON形式

        ijin_name = dict_["ijin_name"]
        input_text = dict_["input_text"]

        nlp_result_dict = {
            "score": str(NLP_main.main(ijin_name, input_text)),
            # TODO テンプレ表示用。セッションで持ち回る場合は不要
        }

        return Response(nlp_result_dict)


    # def put(self, request, format=None):
    #     pass

    # def delete(self, request, format=None):
    #     pass
