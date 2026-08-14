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

- このリポジトリは manabibashi の REPO_STANDARD.md に準拠する。手元に無ければ
  `gh api repos/manabibashi/.github/contents/REPO_STANDARD.md -H "Accept: application/vnd.github.raw+json"` で取得
- ブランチは main のみ。作業は短命ブランチ → PR → squash。force push・ブランチ削除・
  リポジトリ設定変更などの破壊的操作はユーザー確認必須
- 例外【A-4】: マージ済み**ローカル**ブランチは、① `git fetch --prune` 後に upstream が gone
  ② 対応 PR がマージ済み(`gh pr list --state merged --head <branch>`)
  ③ ブランチ先端 SHA が当該 PR の headRefOid と一致、または PR のコミット一覧
  (`gh pr view <番号> --json commits --jq '.commits[].oid'`)に含まれる(未 push コミット無し。
  PR の「Update branch」で main を取り込むと headRefOid はローカルに無いマージコミットになる)
  の 3 条件を検証できた場合のみ、確認なしで `git branch -D` で削除してよい
  (squash 運用のため `-d` は失敗する)。リモートブランチの削除は対象外(確認必須のまま)
- push / マージの最終実行はユーザー判断。Claude Code は PR 作成まで
- タスク・ステータスは GitHub Issues で管理する。backlog.md 等の独自ファイルを作らない
- GitHub Actions を書く際は各 action の最新メジャーを確認してから使う。
  Node 20 世代(actions/checkout@v4 等)を新規に書かない

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
