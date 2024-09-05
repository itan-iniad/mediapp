from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .llm_model import diagnose  # LLM用のスクリプトをインポート

# 診断を処理するビュー
def diagnose_view(request):
    if request.method == "POST":
        symptoms = request.POST.get("symptoms")
        diagnosis = diagnose(symptoms)  # LLMで診断を実施
        return render(request, "result.html", {"diagnosis": diagnosis})
    return render(request, "diagnose.html")
