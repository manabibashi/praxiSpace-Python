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

- この節は REPO_STANDARD.md 付録 D の一字一句のコピー。**リポジトリ固有の注記をここに書き足さない**
  (書くなら下のリポジトリ固有の節へ)。共通節は改訂のたびに機械的に差し替えるため書き足しは失われる
- このリポジトリは manabibashi の REPO_STANDARD.md に準拠する。手元に無ければ
  gh api repos/manabibashi/.github/contents/REPO_STANDARD.md -H "Accept: application/vnd.github.raw+json" で取得
- ブランチは main のみ。作業は短命ブランチ → PR → squash。force push・ブランチ削除・
  リポジトリ設定変更などの破壊的操作はユーザー確認必須
- 例外【A-4】: マージ済み**ローカル**ブランチは、① `git fetch --prune` 後に upstream が gone
  ② 対応 PR がマージ済み(`gh pr list --state merged --head <branch>`)
  ③ ブランチ先端 SHA が当該 PR の headRefOid と一致、または PR のコミット一覧
  (`gh pr view <番号> --json commits --jq '.commits[].oid'`)に含まれる
  の 3 条件を検証できた場合のみ、確認なしで `git branch -D` で削除してよい
  (squash 運用のため `-d` は失敗する)。③が成立していれば未 push コミットが無いことも保証される。
  ③に「または」が必要なのは、PR の「Update branch」で main を取り込むと headRefOid が
  ローカルに無いマージコミットになり、先端 SHA と一致しなくなるため。
  リモートブランチの削除は対象外(確認必須のまま)
- ローカル同期【A-5】: `git fetch --prune` はいつでも確認なしで可(A-4 判定前は必須)。
  `git switch main` は作業ツリーがクリーンならいつでも可(A-4 で現在いるブランチを
  削除するための退避を含む)。`git pull --ff-only` による main の更新は新規ブランチを
  切る直前のみ可。それ以外は main が遅れていても放置してよい
- push とマージ【A-6】: Claude Code は作業ブランチの push と PR 作成まで。マージはユーザーが
  実行する。main への直接 push はしない
- 投稿の帰属【A-7】: Claude Code が GitHub に投稿する本文(Issue・PR・コメント・レビュー返信)は
  冒頭に `🤖 Generated with [Claude Code](https://claude.com/claude-code)` を置く。
  コミットは `Co-Authored-By` トレーラーで示す
- タスク・ステータスは GitHub Issues で管理する。backlog.md 等の独自ファイルを作らない
- プラン名や時限的な外部仕様をドキュメントに書かない(書く場合は日付を添える)
- GitHub の参照・操作は GitHub MCP(接続済みなら)または gh CLI を使う
- GitHub Actions を書く際は各 action の最新メジャーを確認してから使う(GitHub MCP または gh api)。
  EOL 予定・EOL 済みのランナー世代を新規に書かない
  (2026-08 時点では Node 20 世代 = actions/checkout@v4 等が該当。Node 20 ランナーは 2026-09-16 に削除)
- この共通節より下に**リポジトリ固有の節を H2 見出しで置く**(名称は任意)。共通節配下の H3 に
  入れ子にしない(共通節を機械的に差し替える際に巻き込まれるため)。そこに dependabot 構成・
  automerge level・デプロイ方式・環境名の由来(ブランチ整理で消してはいけない名前)を記録する

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
