import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# APIキーの登録
os.environ["OPENAI_API_KEY"] = "__YOUR KEY__"

# OpenAI APIベースURL
url = "https://api.openai.iniad.org/api/v1/"

# プロジェクトのルートディレクトリからの絶対パスを取得
base_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(base_dir, "contents/Disease.pdf")

# PDFファイルの読み込み
loader = PyPDFLoader(pdf_path)
text = "\n".join([page.page_content for page in loader.load()])

# テキストをチャンクに分割
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=20)
documents = text_splitter.create_documents([text])

# OpenAIの埋め込みモデルを使用してベクトル化
embeddings_model = OpenAIEmbeddings(openai_api_base=url)
db = Chroma.from_documents(documents, embeddings_model)

# retriever（検索対象のVectorDB）
retriever = db.as_retriever()

# LLMの定義
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, openai_api_base=url)

# プロンプトテンプレートの定義
template = """以下の症状から考えられる病名を教えてください:

{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

# Chainの定義
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def diagnose_with_rag(symptoms):
    # LLMとRAGを使って診断を実行
    output_by_retriever = chain.invoke(symptoms)
    return output_by_retriever
