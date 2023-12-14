## Gemini Pro Streamlit app

[Gemini Pro](https://ai.google.dev/) を使った Streamlit アプリケーションです。

### 実行方法

```bash
curl -sSL https://install.python-poetry.org | python3 -
portry install
poetry run streamlit run app.py
```

### 環境変数

- GOOGLE_API_KEY : Gemini API の API キー

[Google AI Studio](https://makersuite.google.com/)から取得した API キーを設定してください。
