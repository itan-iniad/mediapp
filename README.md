# AIに基づいた病名診断サポートアプリ ***Mediface***

INIAD(東洋大学情報連携学部)の夏季集中講義「ICT社会応用論D」にて、DjangoとChatGPT APIとlangchainと〜って使ってRAGがどうのこうの〜ってやったWebアプリです。

以下の3ファイル内の `os.environ["OPENAI_API_KEY"] = "__YOUR KEY__"` の `__YOUR KEY__` の部分は、各自で発行したAPIキーを用いてください。

- `mediface/diagnosis/` 下の `llm_model.py` `rag_model.py`
- `test-code/` 下の `learn_document.ipynb`

なお、本アプリはINIADの学内での使用を想定しています。そのため、APIを叩く先のURLもINIADのものとなっております。INIADのAI-MOPではなく、OpenAIの方のAPIを直接叩きに行きたい場合は、適宜URLを書き換えてください。(それで動くかは知りません)

## 環境構築

- Windowsの場合
  - Cloneする
↓
  - コマンドプロンプト(Powershell)でクローンしたディレクトリまで行く
↓
  - `python -m venv venv`
を入力
↓
  - `.\venv\Scripts\activate`
を入力
`(venv)X:\~~`になったら成功
↓
  - `pip install django requests openai markdown langchain langchain-community langchain_openai pypdf tiktoken chromadb`
を入力

- Ubuntuの場合
  - Cloneする
↓
  - bashでクローンしたディレクトリまで行く
↓
  - `python3 -m venv venv`
を入力
↓
  - `source venv/bin/activate`
を入力
`(venv)~~:~$`になったら成功
↓
  - `pip install django requests openai markdown langchain langchain-community langchain_openai pypdf tiktoken chromadb`
を入力
