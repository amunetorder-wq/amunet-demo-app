import streamlit as st
import pandas as pd

st.title("AMU-NET システムデモ")
st.write("これは自動化システムやデータ処理の動作デモ画面です。")

# サンプルデータの表示
data = {"対応エリア": ["尼崎市", "西宮市", "大阪市"], "対応件数": [150, 85, 42]}
df = pd.DataFrame(data)
st.dataframe(df)

if st.button("テスト処理を実行"):
    st.success("正常にシステムが稼働しています！")