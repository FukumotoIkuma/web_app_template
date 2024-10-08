# webアプリケーションテンプレート

全画面で動作するwebアプリケーションを作成するための簡単なテンプレート

## 前提

ブラウザゲームで見かける全画面モードは、画面遷移（すなわち、URLの変更を伴う遷移）を行うと解除される。この仕様を回避しつつ画面遷移を行うテンプレートになっている。

## 各フォルダ・ファイルの詳細

### app.py

flaskアプリケーションの典型である。各遷移先を通常通り実装する。
このURLに直接アクセスしてもhtmlファイルが表示されるだけで動かない。cssが読み込まれないのであまり面白味はない。

一般アクセスを弾く仕組みを実装しても良いだろう。

### static

css用のフォルダである。

### template

htmlフォルダである。
`index.html`はアプリケーション用のhtmlである。詳細は次項。その他は遷移先のファイルである。

## `index.html`
主にアプリケーションの初期化を行なっている。
- headにおいてcssファイルを読み込んでいる
- 各htmlファイル間で相互に遷移するための関数を定義している
- 画面右下最前に、画面最大化ボタンを配置している。解除方法はESCキーのみとなっている。

その後、アプリケーションのメインページを読み込んでいる。