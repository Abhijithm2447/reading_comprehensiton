from django.shortcuts import render
from django.views.generic import View
from rc_app.mixins import HttpResponseMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rc_app.rc_handler import RCPrediction

@method_decorator(csrf_exempt, name='dispatch')
class RCView(View, HttpResponseMixin):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from get method'})
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request["POST"]
        question = data["question"]
        context = data["context"]
        answer = RCPrediction().answer(question, context)
        json_data = json.dumps({'answer': answer})
        return self.render_to_http_response(json_data)
