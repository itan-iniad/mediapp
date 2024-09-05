from django.shortcuts import render

# Create your views here.
import markdown
from django.shortcuts import render
from .llm_model import diagnose  # llm_modelからdiagnose関数をインポート

# 診断を処理するビュー
def diagnose_view(request):
    if request.method == "POST":
        symptoms = request.POST.get("symptoms")

        markdown_diagnosis = diagnose(symptoms)  # LLMを使ってMarkdown形式で診断を取得

        # Markdown形式をHTMLに変換
        html_diagnosis = markdown.markdown(markdown_diagnosis)

        return render(request, "diagnosis/result.html", {"diagnosis": html_diagnosis})
    return render(request, "diagnosis/diagnose.html")

def mapapi_view(request):
    return render(request, "diagnosis/mapapi.html")