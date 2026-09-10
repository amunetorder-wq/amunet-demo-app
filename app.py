import streamlit as st
import pandas as pd
import time

# ページ全体の設定
st.set_page_config(page_title="AMU-NET システムカタログ", layout="centered")

st.subheader("AMU-NET 開発システムカタログ")
st.write("各タブをクリックして、システムの導入効果をご覧ください。")

tab1, tab2, tab3 = st.tabs(["🏢 AI名刺OCR", "👾 シンデレラ作戦", "📄 PDF自動処理"])

# --- 1. 名刺OCRデモ ---
with tab1:
    st.markdown("### 「スマホで撮るだけ。名刺管理をAIで完全自動化」")
    st.write("Gemini APIの高度な文字認識機能を活用し、名刺のデジタル化からリスト作成までを一瞬で完了させます。")
    
    st.markdown("""
    | 導入前（これまでの課題） | 導入後（CardConnectの解決策） |
    | :--- | :--- |
    | いただいた名刺がデスクに山積み... | スマホで撮影するだけで即座にデータ化！ |
    | Excelへの手入力に毎回時間がかかる | AIが読み取り、スプレッドシートへ自動入力！ |
    | 担当者しか顧客の連絡先を知らない | クラウド上で営業チーム全体へ瞬時にリスト共有！ |
    """)
    
    st.info("💡 **高精度なAI読み取り**: 複雑なレイアウトの名刺でも会社名・氏名・連絡先を正確に抽出します。\n\n💡 **既存システムとの連携**: 独自アプリは不要。普段お使いのGoogleスプレッドシートに直接蓄積されます。")

    st.markdown('**【簡易動作デモ】**')
    if st.button("名刺読み取りデモを実行", use_container_width=True):
        with st.spinner("AIが文字を読み取り、スプレッドシートへ送信中..."):
            time.sleep(1.5)
        st.success("✅ データ化と連携が完了しました！")
        sample_data = {
            "項目": ["会社名", "氏名", "役職", "電話番号", "メール"],
            "読み取り結果": ["株式会社AMU-NET", "沼 浩平", "代表", "090-XXXX-XXXX", "amunet.order@gmail.com"]
        }
        st.table(pd.DataFrame(sample_data))


# --- 2. エンタメアプリデモ ---
with tab2:
    st.markdown("### 「遊び心が顧客を掴む。16bitドット絵の接客エンタメツール」")
    st.write("飲食店やナイトレジャー店舗のコンセプトに合わせて、お客様を飽きさせないインタラクティブな体験を提供します。")
    
    st.markdown("""
    | アピールポイント | 詳細 |
    | :--- | :--- |
    | **他店との圧倒的な差別化** | 「お堅い業務システム」の枠を超え、レトロRPG風のUIでお客様の目を引きます。 |
    | **接客のコミュニケーション** | 画面のコマンドをお客様と一緒に操作することで、自然な会話のきっかけを生み出します。 |
    | **完全オリジナルカスタマイズ** | 店舗の雰囲気やスタッフのキャラクターに合わせたドット絵・テキストの変更が可能です。 |
    """)

    st.info("💡 **直感的な操作性**: スマホやタブレットから、誰でもゲーム感覚で楽しく操作できます。\n\n💡 **ブランド価値の向上**: 「面白いシステムを入れているお店」として、SNSでの口コミやリピート率向上に貢献します。")

    st.markdown('**【簡易動作デモ】**')
    st.write("▶ コマンドをせんたくしてください")
    cmd_col1, cmd_col2 = st.columns(2)
    with cmd_col1:
        if st.button("⚔️ たたかう", use_container_width=True):
            st.error("しかし なにも おこらなかった！")
        if st.button("🛡️ ぼうぎょ", use_container_width=True):
            st.warning("ぼうぎょの かまえ！")
    with cmd_col2:
        if st.button("🔮 じゅもん", use_container_width=True):
            st.balloons()
            st.success("まほうが かかった！")
        if st.button("🏃 にげる", use_container_width=True):
            st.info("うまく にげきれた！")


# --- 3. 業務自動化デモ ---
with tab3:
    st.markdown("### 「毎月の『面倒な事務作業』をゼロに」")
    st.write("大量の請求書や納品書PDFから必要なテキスト情報を自動で抽出し、指定のルールに従ってファイル名の変更と仕分けを行います。")
    
    st.markdown("""
    | 業務のビフォー | 自動化のアフター |
    | :--- | :--- |
    | 1件ずつPDFを開いて取引先名を確認 | フォルダ内の全PDFを一括でAIが自動読み取り |
    | 手作業で「年月_会社名_請求書」と入力 | 抽出したテキストから正しいファイル名を自動生成 |
    | 取引先ごとのフォルダへ手動で移動 | ルールに基づき、指定のフォルダへ一瞬で自動振り分け |
    """)
    
    st.info("💡 **ヒューマンエラーの防止**: 手作業による入力ミスや、保存先フォルダの間違いを完全に防ぎます。\n\n💡 **大幅なコスト削減**: 毎月数時間かかっていた単純作業を数秒で終わらせ、コア業務に集中できます。")

    st.markdown('**【簡易動作デモ】**')
    st.write("処理対象のファイル（ダミーデータ）")
    before_files = pd.DataFrame({"元のファイル名": ["doc_001.pdf", "doc_002.pdf", "doc_003.pdf"]})
    st.dataframe(before_files, use_container_width=True)
    
    if st.button("一括自動処理を実行", use_container_width=True):
        with st.spinner('AIが内容を解析し、リネーム中...'):
            time.sleep(1.5)
        st.success("3件のPDF処理が完了しました！")
        after_files = pd.DataFrame({
            "変更後のファイル名": ["202609_株式会社A様_請求書.pdf", "202609_B商事様_請求書.pdf", "202609_C工業様_請求書.pdf"],
            "ステータス": ["✅ 完了", "✅ 完了", "✅ 完了"]
        })
        st.dataframe(after_files, use_container_width=True)