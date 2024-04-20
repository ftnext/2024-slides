:ogp_title: VS Codeで文字列のちょっとした変換ができるんです！
:ogp_event_name: vscodeconjp
:ogp_slide_name: transform-text-commands
:ogp_description: 〜実装まで覗くクイックツアー〜 2024/04 VS Code Conference JP
:ogp_image_name: vscodeconjp

======================================================================
VS Codeで文字列のちょっとした変換ができるんです！
======================================================================

〜実装まで覗くクイックツアー〜

VS Codeで文字列のちょっとした変換ができるんです！
======================================================================

〜実装まで覗くクイックツアー〜

:Event: VS Code Conference JP 2024
:Presented: 2024/04/20 nikkie

お前、誰よ（自己紹介）
======================================================================

* nikkie ／ 毎日 `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 執筆、520日突破
* ソフトウェアエンジニアリングで突破するデータサイエンティスト（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* 仕事もプライベートも **VS Code** で **Python** と戯れています

.. image:: ../_static/uzabase-white-logo.png

1年ぶりですね
--------------------------------------------------

`VS Code Conference Japan 2022 - 2023で15分2本登壇しました <https://nikkie-ftnext.hatenablog.com/entry/talked-vscode-conference-jp-2023>`__

* `楽々入門！VS Codeで『リファクタリング』 <https://ftnext.github.io/2023-slides/vscodeconjp/introduction-easy-refactoring.html>`__
* `Awakening Extension (拡張開発はじまるよ🔰) <https://ftnext.github.io/2023-slides/vscodeconjp/awakening-extension.html>`__

.. 自作のVS Code拡張？

このトークでは（`fortee <https://fortee.jp/vscodeconjp-2024/proposal/752a18a4-7a34-4eec-9d7e-4d4169e7ee43>`__）
------------------------------------------------------------------------------------------------------------------------------------------------------

* VS Codeで **文字列のちょっとした変換** をする方法を紹介
* どのように実装されているか、少しだけ覗いてみよう（*実装の話*）

.. include:: vscode-commands.rst.txt

🌯まとめ：VS Codeで文字列のちょっとした変換ができるんです！
======================================================================

1. テキストを選択
2. コマンドパレット
3. :guilabel:`Transform to` コマンド

完
--------------------------------------------------

文字列のちょっとした変換にVS Codeを使ってみてください！

VS Codeで文字列のちょっとした変換ができるんです！
======================================================================

〜 **実装まで覗くクイックツアー** 〜

.. include:: implementation-quick-tour.rst.txt

🌯まとめ：VS Codeで文字列のちょっとした変換ができるんです！
======================================================================

* **コマンドパレット** の :guilabel:`Transform to` コマンドで文字列を変換できる
* コマンドごとにActionクラス。 ``_modifyText()`` を実装する **Template Method** パターン
* Unicode文字クラスエスケープをはじめ、正規表現を駆使

ご清聴ありがとうございました
--------------------------------------------------

コマンドパレットで Enjoy coding!✨

EOF
======================================================================
