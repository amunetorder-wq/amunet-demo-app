import streamlit as st
import pandas as pd

# ページ全体の設定
st.set_page_config(page_title="AMU-NET システムデモ", layout="wide")

# --- サイドバー（メニュー）の設定 ---
st.sidebar.title("AMU-NET デモメニュー")
st.sidebar.write("ご覧になりたいシステムを選択してください。")
# ラジオボタンで3つのメニューを作成
selected_demo = st.sidebar.radio(
    "",
    ["1. AI名刺デジタル化 (CardConnect)", 
     "2. 店舗向けエンタメ (シンデレラ作戦)", 
     "3. PDF帳票自動処理ツール"]
)

# --- 各デモ画面のコンテンツ ---

# 1. 名刺OCRデモ
if selected_demo == "1. AI名刺デジタル化 (CardConnect)":
    st.header("🏢 AI名刺デジタル化システム (CardConnect)")
    st.write("Gemini APIを活用し、スマートフォンで撮影した名刺画像を瞬時にテキストデータ化。Googleスプレッドシートへ自動連携する顧客管理ツールです。")
    
    st.info("※現在デモモードのため、サンプルの読み取り結果を表示しています。")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("【仮想アップロード画像】")
        # ダミーの枠を表示
        st.markdown('<div style="height:200px; background-color:#f0f2f6; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#555;">[ 名刺の画像ファイル ]</div>', unsafe_allow_html=True)
        st.button("AIで解析する")
        
    with col2:
        st.write("【AI解析結果（デモ）】")
        sample_data = {
            "項目": ["会社名", "氏名", "役職", "電話番号", "メール"],
            "読み取り結果": ["株式会社AMU-NET", "沼 浩平", "代表", "090-XXXX-XXXX", "amunet.order@gmail.com"]
        }
        st.table(pd.DataFrame(sample_data))


# 2. エンタメアプリデモ
elif selected_demo == "2. 店舗向けエンタメ (シンデレラ作戦)":
    st.header("👾 店舗向けエンタメアプリ (シンデレラ作戦)")
    st.write("飲食店やナイトレジャー店舗での接客ツールとして開発。16bitのレトロRPG風ドット絵UIを採用し、お客様に楽しんでいただけるインタラクティブなアプリです。")
    
    st.success("「システム＝お堅い」という常識を覆し、店舗のコンセプトに合わせた遊び心のあるデザインも可能です。")
    
    # 簡易的なRPG風の選択肢ボタン
    st.write("▶ コマンドをせんたくしてください")
    cmd_col1, cmd_col2, cmd_col3, cmd_col4 = st.columns(4)
    with cmd_col1:
        if st.button(" ⚔️ たたかう "):
            st.error("しかし なにも おこらなかった！")
    with cmd_col2:
        if st.button(" 🔮 じゅもん "):
            st.balloons()
            st.success("まほうが かかった！")
    with cmd_col3:
        st.button(" 🛡️ ぼうぎょ ")
    with cmd_col4:
        st.button(" 🏃 にげる ")


# 3. 業務自動化デモ
elif selected_demo == "3. PDF帳票自動処理ツール":
    st.header("📄 PDF帳票自動処理・リネームツール")
    st.write("毎日の煩雑な事務作業をPythonで自動化。大量のPDF請求書から顧客名などを抽出し、ルールに従って自動でファイル名を変更・仕分けします。")
    
    st.warning("※これは処理のイメージを再現したデモです。")
    
    st.write("【処理対象のファイル（サンプル）】")
    before_files = pd.DataFrame({"元のファイル名": ["doc_001.pdf", "doc_002.pdf", "doc_003.pdf"]})
    st.dataframe(before_files, use_container_width=True)
    
    if st.button("一括自動処理を実行"):
        with st.spinner('AIが内容を解析し、リネーム中...'):
            import time
            time.sleep(1.5) # 処理中を演出
        
        st.success("3件のPDF処理が完了しました！")
        after_files = pd.DataFrame({
            "変更後のファイル名": ["202609_株式会社A様_請求書.pdf", "202609_B商事様_請求書.pdf", "202609_C工業様_請求書.pdf"],
            "ステータス": ["✅ 完了", "✅ 完了", "✅ 完了"]
        })
        st.dataframe(after_files, use_container_width=True)