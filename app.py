import streamlit as st
import pandas as pd

# ページ全体の設定
st.set_page_config(page_title="AMU-NET システムデモ", layout="centered")

st.subheader("AMU-NET システムデモ")
st.write("ご覧になりたいシステムを上のタブから選択してください。")

# サイドバーではなく、画面上部の「タブ」で切り替える形式に変更
tab1, tab2, tab3 = st.tabs([
    "🏢 AI名刺OCR", 
    "👾 エンタメ (シンデレラ作戦)", 
    "📄 PDF自動処理"
])

# --- 1. 名刺OCRデモ ---
with tab1:
    st.write("Gemini APIを活用し、スマートフォンで撮影した名刺画像を瞬時にテキストデータ化。Googleスプレッドシートへ自動連携する顧客管理ツールです。")
    st.info("※現在デモモードのため、サンプルの読み取り結果を表示しています。")
    
    st.markdown('**【仮想アップロード画像】**')
    st.markdown('<div style="height:150px; background-color:#f0f2f6; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#555; margin-bottom: 10px;">[ 名刺の画像ファイル ]</div>', unsafe_allow_html=True)
    
    # ボタンを横幅いっぱいに広げる
    st.button("AIで解析する", key="ocr_btn", use_container_width=True)
    
    st.markdown('**【AI解析結果（デモ）】**')
    sample_data = {
        "項目": ["会社名", "氏名", "役職", "電話番号", "メール"],
        "読み取り結果": ["株式会社AMU-NET", "沼 浩平", "代表", "090-XXXX-XXXX", "amunet.order@gmail.com"]
    }
    st.table(pd.DataFrame(sample_data))

# --- 2. エンタメアプリデモ ---
with tab2:
    st.write("飲食店やナイトレジャー店舗での接客ツールとして開発。16bitのレトロRPG風ドット絵UIを採用し、お客様に楽しんでいただけるアプリです。")
    st.success("「システム＝お堅い」という常識を覆し、店舗のコンセプトに合わせたデザインも可能です。")
    
    st.write("▶ コマンドをせんたくしてください")
    
    # 4列だと文字が切れるため、2列×2段に変更し、ボタンを枠いっぱいに広げる
    cmd_col1, cmd_col2 = st.columns(2)
    with cmd_col1:
        if st.button("⚔️ たたかう", use_container_width=True):
            st.error("しかし なにも おこらなかった！")
        if st.button("🛡️ ぼうぎょ", use_container_width=True):
            st.info("ぼうぎょの かまえ！")
    with cmd_col2:
        if st.button("🔮 じゅもん", use_container_width=True):
            st.balloons()
            st.success("まほうが かかった！")
        if st.button("🏃 にげる", use_container_width=True):
            st.warning("うまく にげきれた！")

# --- 3. 業務自動化デモ ---
with tab3:
    st.write("毎日の煩雑な事務作業をPythonで自動化。大量のPDF請求書から顧客名などを抽出し、ルールに従って自動でファイル名を変更・仕分けします。")
    st.warning("※これは処理のイメージを再現したデモです。")
    
    st.write("【処理対象のファイル（サンプル）】")
    before_files = pd.DataFrame({"元のファイル名": ["doc_001.pdf", "doc_002.pdf", "doc_003.pdf"]})
    st.dataframe(before_files, use_container_width=True)
    
    if st.button("一括自動処理を実行", use_container_width=True):
        with st.spinner('AIが内容を解析し、リネーム中...'):
            import time
            time.sleep(1.5)
        
        st.success("3件のPDF処理が完了しました！")
        after_files = pd.DataFrame({
            "変更後のファイル名": ["202609_株式会社A様_請求書.pdf", "202609_B商事様_請求書.pdf", "202609_C工業様_請求書.pdf"],
            "ステータス": ["✅ 完了", "✅ 完了", "✅ 完了"]
        })
        st.dataframe(after_files, use_container_width=True)