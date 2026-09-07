# CLAUDE.md

## このリポジトリの目的

praxiSpace の**子ども向け Python イベント用の学習教材**(公開リポジトリ)です。

- `lecture/` : 講義で使うサンプルコード
- `practice/` : 練習問題の解答例

読むのは子ども・保護者・講師です。プロダクションコードではありません。

## 最優先事項: 教材としての分かりやすさ

**`lecture/` と `practice/` の `.py` ファイルを、頼まれていないのに変更しないこと。**

- 冗長に見える書き方(同じ `append` を3回並べる、`if/else` を明示的に書く等)は、
  初学者に理解しやすくするための**意図的なもの**です。リファクタしないでください。
- 「もっと Pythonic に」「重複を関数化」といった改善提案は不要です。
- バグを見つけた場合も勝手に直さず、**報告だけ**してください。
- 教材コードの変更を依頼された場合は、その回で教えている文法だけを使うこと
  (例: `for` を教える前のファイルで `for` を使わない)。コメントも平易な日本語で書きます。

Python 3.11 で動作を確認しています。

## ブランチ運用

- ブランチは `main` のみ(トランクベース)。`dev` 等は作りません。
- 変更は `main` への直接プルリクエストで行い、**squash** でマージします。
- `main` への直接 push はルールセットで禁止されています。承認は0で通ります。

## 組織共通ルール(REPO_STANDARD 準拠)

- この節は REPO_STANDARD.md 付録 D のコピー。リポジトリ固有の注記はこの下の H2 節に書く
  (共通節は改訂のたびに機械的に差し替えるため、ここへの書き足しは失われる)
- manabibashi の REPO_STANDARD.md に準拠する。手元に無ければ
  gh api repos/manabibashi/.github/contents/REPO_STANDARD.md -H "Accept: application/vnd.github.raw+json" で取得
- ブランチは main のみ。短命ブランチ → PR → squash。Claude Code は push と PR 作成まで、マージはユーザー【A-6】。
  force push・ブランチやタグの削除・リポジトリ設定変更などの破壊的操作はユーザー確認必須
- ローカル同期・マージ済みブランチの掃除・push の範囲・投稿の帰属【A-4〜A-7】は組織プラグイン
  `manabibashi-standard` のフックが担保する。未導入なら REPO_STANDARD §2 / §8 の手順に従い、
  破壊的な git 操作の前に必ずユーザー確認を取る
- PR を作る前に `/code-review` と `/security-review` を実行する(未実施の PR 作成はフックが止める)
- テストを実行できるリポジトリのロジック変更は TDD(失敗するテスト → 実装 → リファクタ)で進める
- 複数行の本文(コミット・PR・Issue・コメント)は Write でファイルに書いて `-F` / `--body-file` で渡す。
  数行を超える処理はシェルに埋め込まず、Node スクリプトをファイルに書いて実行する
- タスク・ステータスは GitHub Issues で管理する。独自のタスクファイルを作らない
- プラン名や時限的な外部仕様をドキュメントに書かない(書くなら日付を添える)
- GitHub の参照・操作は GitHub MCP(接続済みなら)または gh CLI を使う
- GitHub Actions は各 action の最新メジャーを確認して書く。EOL 予定・EOL 済みのランナー世代を新規に書かない
- この共通節より下にリポジトリ固有の節を H2 見出しで置く(共通節配下の H3 に入れ子にしない)。
  そこに dependabot 構成・automerge level・デプロイ方式・環境名の由来を記録する

## CI(リポジトリ固有)

**CI / automerge は共通ワークフロー(`manabibashi/workflows@v1`)の呼び出し**(REPO_STANDARD §5)。
実体は同リポジトリにあり、ここには薄い caller だけを置きます。ジョブ ID `ci` は変更禁止。

- `ci.yml` の `with:` — **`runtime: none`** / `test-command: python3 -m compileall .`
  （リポジトリ全体の `.py` を構文チェック。旧 CI の全ファイル対象と同等）。
  **uv 化はしません**(教材リポジトリに packaging の概念を持ち込まないため。Issue #4 の方針)。
  ubuntu ランナーの system python で動きます。
- 必須ステータスチェック名は **`ci / required-check`**(組織で統一)。
- **automerge level: 3**(実テストが無く構文チェックのみ。REPO_STANDARD §4 / B-4)。
- **lint(ruff 等)は意図的に入れていません。** 教材の意図的な書き方を壊すためです。追加しないでください。
- テストコードはありません。新規に作らないでください。
- `.github/dependabot.yml` は **github-actions のみ**(Python の依存管理ファイルが無いため。B-6)。
  weekly(月曜 09:00 JST)/ cooldown 7 日 / minor+patch をグループ化。
