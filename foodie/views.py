from django.shortcuts import render
from django.views.generic import TemplateView

GNAVI_URL = "https://api.gnavi.co.jp/RestSearchAPI/v3/"
GNAVI_KEY = "e69b765feb7e3902bdc22e281874aa97" # 取得したkeyid

class IndexView(TemplateView):
    template_name = 'foodie/index.html'
