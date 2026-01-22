# SystemControl_2025

JupyterLab 環境構築・利用ガイド
# SystemControl_2025 JupyterLab 環境構築・利用ガイド

このガイドでは、Python環境の構築（pyenv経由）、JupyterLabのインストール、および基本的な利用方法について解説します。

## 1. 環境構築 (Pythonのインストール)

`pip` コマンドが使用できない場合や、まだPythonをインストールしていない場合は、以下の手順で `pyenv` を経由してPythonをインストールしてください。
※すでにインストール済みの方は「2. JupyterLabのインストール」へ進んでください。

### 1-1. pyenvのインストール
ターミナルで以下のコマンドを実行し、`pyenv` をインストールします。

```bash
brew install pyenv
```

### 1-2. 初期設定
インストール後、以下のコマンドを順に実行して環境設定ファイル（`.zshrc`）に必要な設定を追記し、読み込みます。

```bash
touch .zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source .zshrc
```

インストール確認のため、以下を実行してバージョンが表示されるか確認してください。

```bash
pyenv -v
```

### 1-3. Pythonのインストールと設定
今回はバージョン 3.13.7 を使用します。

```bash
pyenv install 3.13.7
pyenv global 3.13.7
```

※ pip install jupyterlab 実行時に pip コマンドが見つからないエラーが出た場合も、上記の pyenv global コマンドを実行してください。


## 2. JupyterLabのインストールと起動

### 2-1. インストール
ターミナルで以下のコマンドを実行します。

```bash
pip install jupyterlab
```

### 2-2. 起動
インストール完了後、以下のコマンドでJupyterLabを起動します。

```bash
jupyter lab
```

## 3. JupyterLabの基本的な使い方
フォルダ・ファイルの作成と管理

フォルダ作成: 左上のタブメニューにある「＋」ボタン（左から2番目）を押して新規フォルダを作成します。

名前の変更: 作成されたフォルダを右クリック（トラックパッド2本指クリック）し、メニューから「Rename」を選択して変更します。

ファイル作成: タブメニュー左端の「＋」ボタンを押し、表示されるメニューから「Notebook」の「Python 3」を選択して作成します。

ノートブックの操作

セルの実行: Shift + Return（Enter） 

改行: Return（Enter） 

カーネルの再起動: 上部メニューの右から2番目のボタン（回転矢印）を押すと、変数の状態などがリセットされ、最初の状態に戻ります 。

セルの種類
セル上部のプルダウンメニューから種類を切り替えることができます 。

Code: Pythonプログラムを記述し、実行するためのセル 。

Markdown: メモ、見出し、箇条書きなどの文章を書くためのセル 。

カーネル（Kernel）とは コードセルの内容を受け取り 、計算を実行し 、その結果やグラフを出力エリアに返す  裏方のプログラムです。


## 4. 日本語化（オプション）
JupyterLabを日本語で使用したい場合は、言語パックをインストールします。

JupyterLabが起動している場合は、ターミナルで Control + C を押して一度終了させます 。

以下のコマンドを実行します 。

pip install jupyterlab jupyterlab-language-pack-ja-JP

再度 jupyter lab コマンドで起動します 。


## 練習問題

range(3) を使ったループ処理で、print のインデント位置による実行結果の違いを確認してみましょう 。

プログラム1: print('python') がループの中にあり、毎回出力される。

プログラム2: print('python') がループの外にあり、最後に1回だけ出力される。