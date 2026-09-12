import streamlit as st
import pandas as pd
import time

# ページ全体の設定
st.set_page_config(page_title="AMU-NET システムカタログ", layout="centered")

st.subheader("AMU-NET 開発システムカタログ")
st.write("各タブをクリックして、システムの導入効果をご覧ください。")

# タブを4つに増やしました
tab1, tab2, tab3, tab4 = st.tabs(["🏢 AI名刺OCR", "👾 シンデレラ作戦", "📄 PDF自動処理", "🛡️ セキュリティ訓練"])

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
    
    if "scene" not in st.session_state:
        st.session_state.scene = 0
        
    scenes = [
        {"img": "1_desert.jpg", "text": "のどが かわいて たおれそうだ..."},
        {"img": "2_guild.jpg", "text": "オアシス（ギルド）に たどりついた！"},
        {"img": "3_tequila.jpg", "text": "テキーラを ちゅうもんした！ テンションUP！"},
        {"img": "4_hungry.jpg", "text": "おなかが すいてきた... なにか たべよう。"},
        {"img": "5_karaoke.jpg", "text": "カラオケで ねっしょうした！"},
        {"img": "6_champagne.jpg", "text": "シャンパンタワー だ！ パーティの はじまりだ！"},
        {"img": "7_clock.jpg", "text": "あっというまに じかんが すぎていく..."},
        {"img": "8_glass.jpg", "text": "グラスを かたむけ、よるが ふけていく..."},
        {"img": "end_good.jpg", "text": "シンデレラ作戦、だいせいこう！"}
    ]

    st.write("▶ コマンドをせんたくしてください")
    cmd_col1, cmd_col2 = st.columns(2)
    
    with cmd_col1:
        if st.button("⚔️ すすむ（アクション）", use_container_width=True):
            if st.session_state.scene < len(scenes) - 1:
                st.session_state.scene += 1
            else:
                st.balloons()
                
    with cmd_col2:
        if st.button("🏃 にげる（最初から）", use_container_width=True):
            st.session_state.scene = 0
            
    current = scenes[st.session_state.scene]
    st.image(current["img"], use_container_width=True)
    st.write(f"**{current['text']}**")

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

# --- 4. Gophish セキュリティ訓練デモ ---
with tab4:
    st.markdown("### 「従業員のセキュリティ意識を劇的に向上。クラウド型標的型攻撃メール訓練」")
    st.write("ランサムウェアなど企業を狙うサイバー攻撃の起点は「従業員へのメール」が大多数です。AMU-NETでは、Google Cloud (GCP) 上に専用の訓練システム『Gophish』を構築し、実践的なセキュリティ教育とインシデント対応体制（CSIRT/SOC）の強化を支援します。")
    
    st.markdown("""
    #### 🛡️ なぜAMU-NETの訓練システムが選ばれるのか？
    * **本番さながらのリアルな訓練:** 取引先や社内通達を装った巧妙な文面を作成し、従業員の「怪しいメールに気づく力」を養います。
    * **GCP環境による安全・低コストな運用:** オープンソースを活用しつつセキュアなクラウドに構築するため、高額なSaaSを導入するよりも大幅にコストを抑えられます。
    * **CSIRTを見据えたインシデント対応訓練:** メールを開いてしまった後の「社内への報告フロー」が迅速に機能するかの実地テストとしても最適です。
    """)
    
    st.info("💡 **導入の流れ**: ヒアリング ＞ 訓練メール文面の作成 ＞ テスト配信 ＞ 本番配信 ＞ 結果レポート提出・振り返り勉強会の実施")

    st.markdown('**【システム画面イメージ：管理者ダッシュボード】**')
    st.write("訓練キャンペーン「2026年 標的型攻撃訓練 (秋季)」の集計結果（デモデータ）")
    
    # 見栄えの良いメトリクス（数値）表示
    col1, col2, col3 = st.columns(3)
    col1.metric(label="送信対象者数", value="50 名")
    col2.metric(label="メール開封率", value="42 %", delta="21名 開封", delta_color="inverse")
    col3.metric(label="リンククリック率", value="12 %", delta="6名 クリック", delta_color="inverse")

    # 部署別クリック率の棒グラフデモ
    st.write("▼ 部署別のクリック率可視化")
    chart_data = pd.DataFrame({
        "部署": ["営業部", "総務部", "製造部", "役員"],
        "クリック率(%)": [18, 5, 15, 0]
    }).set_index("部署")
    st.bar_chart(chart_data)
    
    st.markdown('**【実際の訓練メール文面サンプル】**')
    with st.expander("✉️ 訓練メールのサンプルを見る（クリックして展開）"):
        st.error("件名：【重要】未払い請求書のご確認（株式会社〇〇）")
        st.write("""
        お疲れ様です。経理部の〇〇です。

        先月分の請求書に未払いが確認されました。
        至急、以下のリンクより内容をご確認いただき、本日中にお手続きをお願いいたします。

        👉 [請求書データを確認する (http://fake-link.amu-net.com)](#)

        ※本メールはセキュリティ訓練用のサンプルです。実際の攻撃では巧妙なリンクが設定されます。
        """)
    
    if st.button("📊 詳細な訓練結果レポート（PDF）を生成", use_container_width=True):
        with st.spinner("Gophishサーバーからデータを集計し、レポートを作成中..."):
            time.sleep(1.5)
        st.success("✅ レポートの生成が完了しました。（※本来はここで詳細なPDFがダウンロードされ、経営陣への報告に使用できます）")