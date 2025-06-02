# 書店システム用XMLデータ変換ツール

## プロジェクト内容
書店の書籍カタログXMLファイルをJSON形式に変換するデータ変換ツールです。XMLデータの読み込み、パーシング、JSON変換、ファイル保存まで一連の処理を自動化し、書店システムのデータ管理を効率化します。PythonによるXML処理とJSONデータ変換技術を学習することを目的として実装しました。

## プロジェクト構成
```
bookstore_converter/
├── src/
│   └── data_converter.py    # メインプログラム
├── sample_data/
│   └── books_catalog.xml    # サンプル書籍データ
├── converted_data/          # 変換結果出力フォルダ
├── requirements.txt         # 依存関係管理
├── README.md               # プロジェクト説明書
└── .gitignore              # Git除外ファイル設定
```

## 必要要件/開発環境
- **Python 3.7以上**
- **VSCode** (開発環境)
- **Git** (バージョン管理)

### 使用ライブラリ
- **xmltodict** XMLデータの辞書変換処理
- **json** JSON形式データの変換・保存処理
- **os** ファイルシステム操作

## 機能
- **XMLファイル読み込み** 書籍カタログXMLの自動読み込み
- **データ構造解析** XMLデータの階層構造を辞書形式に変換
- **JSON形式変換** 辞書データをJSON文字列に変換
- **ファイル自動保存** 変換結果を指定フォルダに保存
- **フォルダ自動作成** 出力フォルダの存在確認と自動作成
- **変換結果確認** 保存されたJSONファイルの内容検証
- **エラーハンドリング** ファイル操作や変換処理のエラー対応
- **ファイルサイズ確認** 変換後ファイルのサイズ表示

## 実行方法

### 1. リポジトリのクローン
```bash
git clone https://github.com/yourusername/bookstore_converter.git
cd bookstore_converter
```

### 2. 仮想環境の作成・アクティベート

**Windows**
```bash
python -m venv myenv
myenv\Scripts\activate
```

**macOS**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 4. プログラムの実行
```bash
python src/data_converter.py
```

実行後、sample_data/books_catalog.xmlがJSONファイルに変換され、converted_dataフォルダに保存されます。

## データ形式について
- **入力データ** XML形式の書籍カタログファイル
- **出力データ** JSON形式の変換済みデータファイル
- **サンプルデータ** 8冊の書籍情報を含む実データ

## 開発者
YuYu