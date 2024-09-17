=============================================================================================================
PEP 723（Inline script metadata）が拓く世界。Pythonスクリプトに必要な仮想環境をツールにおまかせできるんです！
=============================================================================================================

**プレビュー版**：PEP 723（Inline script metadata）が拓く世界。Pythonスクリプトに必要な仮想環境をツールにおまかせできるんです！
==================================================================================================================================

:Event: みんなのPython勉強会#108 LT
:Presented: 2024/09/19 nikkie

このLTは
--------------------------------------------------

* 2024/09/27(金) 28(土) に有明で開催される `PyCon JP 2024 <https://pyconjp.connpass.com/event/324211/>`__ のトークのプレビューです

  * `金曜 15:50〜 20F #pyconjp_1 <https://2024.pycon.jp/ja/talk/89F3RQ>`__ 僕と握手🤝

* お届けする内容は、ちょっとした **スクリプトを書くシーン** で皆さんに使ってもらえたら嬉しいです

サンプルスクリプト
======================================================================

* PEP＝ `Python Enhancement Proposal <https://docs.python.org/ja/3/glossary.html#term-PEP>`__ （Pythonの機能提案文書） 
* PEPの一覧をJSON形式で取得できると知ったのでやってみたい

このライブラリを使おうかな
--------------------------------------------------

* `httpx <https://github.com/encode/httpx>`__ ：HTTPクライアント（`金曜 16:40〜 20F #pyconjp_2 <https://2024.pycon.jp/ja/talk/MD99N8>`__）
* `rich <https://github.com/Textualize/rich>`__ ：ターミナルにリッチなテキストで出力

試す際はお好みのライブラリに読み替えください

PEPの一覧をJSON形式で取得するスクリプト
--------------------------------------------------

.. literalinclude:: ../../samplecode/inline-script-metadata/example_like_pep723.py
    :language: python
    :lines: 4-9
    :caption: example.py

スクリプト動かす前に仮想環境作ろう！
--------------------------------------------------

.. TODO Python 3.12で最新化

.. code-block:: shell

    $ python -V
    Python 3.12.2
    $ python -m venv .venv --upgrade-deps
    $ .venv/bin/python -m pip install httpx rich
    $ .venv/bin/python example.py

仮想環境で実行したスクリプトの出力
--------------------------------------------------

.. TODO 画像のほうがいいかも

.. code-block:: txt

    [
    │   ('1', 'PEP Purpose and Guidelines'),
    │   ('2', 'Procedure for Adding New Modules'),
    │   ('3', 'Guidelines for Handling Bug Reports'),
    │   ('4', 'Deprecation of Standard Modules'),
    │   ('5', 'Guidelines for Language Evolution'),
    │   ('6', 'Bug Fix Releases'),
    │   ('7', 'Style Guide for C Code'),
    │   ('8', 'Style Guide for Python Code'),
    │   ('9', 'Sample Plaintext PEP Template'),
    │   ('10', 'Voting Guidelines')
    ]

テキストは緑色で表示されていることでしょう

実は、**私たちが仮想環境を作らなくてもいい** んです！
======================================================================

* タイトルにある「PEP 723（Inline script metadata）」
* スクリプトにコメントとしてメタデータを書き、それをサポートしたツールで実行

Inline script metadata（冒頭のコメント）
--------------------------------------------------

.. literalinclude:: ../../samplecode/inline-script-metadata/example_like_pep723.py
    :language: python
    :emphasize-lines: 1-3
    :caption: example.py（更新版）

Inline script metadataをサポートするツールで実行
------------------------------------------------------------

.. code-block:: shell

    $ pipx run example.py
    $ # または
    $ uv run example.py

ツールが仮想環境を用意して実行！
--------------------------------------------------

.. code-block:: txt

    % uv run example.py
    Reading inline script metadata from: example.py
    Installed 11 packages in 23ms
    [
    │   ('1', 'PEP Purpose and Guidelines'),
    │   ('2', 'Procedure for Adding New Modules'),
    │   ('3', 'Guidelines for Handling Bug Reports'),
    │   ('4', 'Deprecation of Standard Modules'),
    │   ('5', 'Guidelines for Language Evolution'),
    │   ('6', 'Bug Fix Releases'),
    │   ('7', 'Style Guide for C Code'),
    │   ('8', 'Style Guide for Python Code'),
    │   ('9', 'Sample Plaintext PEP Template'),
    │   ('10', 'Voting Guidelines')
    ]

このトークで伝えたいこと
======================================================================

* Pythonスクリプトを書くとき、**Inline script metadataをぜひ使って** みて！
* スクリプトが依存するライブラリをコメントとして書くだけ
* 開発者が仮想環境の管理から解放されます！

続きは9/27(金)のPyCon JP 2024にて
--------------------------------------------------

`金曜 15:50〜 20F #pyconjp_1 <https://2024.pycon.jp/ja/talk/89F3RQ>`__

ご清聴ありがとうございました

お前、誰だったのよ？ ― nikkieでした
--------------------------------------------------

* :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続 **670** 日突破
* ユーザベースの機械学習エンジニア（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `みんなのPython勉強会 <https://startpython.connpass.com/>`__ スタッフ・4代目LT王子
* 小さなOSSの開発が好き：代表作はSphinx拡張 `sphinx-new-tab-link <https://github.com/ftnext/sphinx-new-tab-link>`__

EOF
---
