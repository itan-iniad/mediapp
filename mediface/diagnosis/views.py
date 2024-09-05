from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import markdown
from .rag_model import diagnose_with_rag  # RAGモデルの関数をインポート

# チャット診断を処理するビュー
def chat_diagnose_view(request):
    if request.method == "POST":
        symptoms = request.POST.get("symptoms")
        markdown_diagnosis = diagnose_with_rag(symptoms)  # RAGを使ってMarkdown形式で診断を取得
        html_diagnosis = markdown.markdown(markdown_diagnosis)
        return render(request, "diagnosis/result.html", {"diagnosis": html_diagnosis})
    return render(request, "diagnosis/diagnose.html")

# 問診票診断を処理するビュー
def question_diagnose_view(request):
    if request.method == "POST":
        # 問診票のデータを取得
        age_group = request.POST.get("age_group")
        main_symptom = request.POST.get("main_symptom")
        symptom_duration = request.POST.get("symptom_duration")
        symptom_onset = request.POST.get("symptom_onset")
        pain_scale = request.POST.get("pain_scale")
        symptom_duration_continuity = request.POST.get("symptom_duration_continuity")
        symptom_change = request.POST.get("symptom_change")
        additional_symptoms = request.POST.getlist("additional_symptoms")
        triggers = request.POST.getlist("triggers")
        remarks = request.POST.get("remarks")  # 備考欄のデータを取得

        # 収集したデータをRAGモデルに渡して診断
        combined_input = f"""
        年代: {age_group}, 
        主症状: {main_symptom}, 
        症状の期間: {symptom_duration}, 
        症状の現れ方: {symptom_onset}, 
        痛みの強さ: {pain_scale}, 
        症状の継続性: {symptom_duration_continuity}, 
        症状の変化: {symptom_change}, 
        追加症状: {', '.join(additional_symptoms)}, 
        トリガー: {', '.join(triggers)}, 
        備考: {remarks}
        """
        markdown_diagnosis = diagnose_with_rag(combined_input)
        html_diagnosis = markdown.markdown(markdown_diagnosis)

        return render(request, "diagnosis/result.html", {"diagnosis": html_diagnosis})

    return render(request, "diagnosis/question.html")


def mapapi_view(request):
    return render(request, "diagnosis/mapapi.html")
