:ogp_title: one obvious wayを志向するPythonに依存ライブラリ管理ツールがたっくさんある話
:ogp_event_name: techramen
:ogp_slide_name: python-package-management-tools
:ogp_description: 〜Rust製ツールが高速を謳う〜 TechRAMEN 2024 Conference 前夜祭
:ogp_image_name: techramen

================================================================================
one obvious wayを志向するPythonに依存ライブラリ管理ツールがたっくさんある話
================================================================================

one obvious wayを志向するPythonに依存ライブラリ管理ツールがたっくさんある話
================================================================================

〜Rust製ツールが高速を謳う〜

:Event: TechRAMEN 2024 Conference 前夜祭
:Presented: 2024/07/26 nikkie

nikkie（にっきー）と申します
======================================================================

* 東京から来ました。初旭川
* ソフトウェアエンジニアリングで突破するデータサイエンティスト（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* Python歴6年。PyConで登壇多数

.. image:: ../_static/uzabase-white-logo.png

.. revealjs-break::

* `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続610日突破

  * ♨️ `ばんくしさんによる「ゼロから作る自作 Python Package Manager 入門」がほんとよい！ 写経を積みます <https://nikkie-ftnext.hatenablog.com/entry/vaaaaanquish-python-package-manager-diy-introduction-is-awesome>`__

* :fab:`twitter` `@ftnext <https://twitter.com/ftnext>`__ ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ アニメ好き

Pythonは使いますか？
--------------------------------------------------

実務でも🙋‍♂️ 趣味でも🙋‍♀️

今日の話は **Pythonのライブラリを管理** する話
--------------------------------------------------

* どんなプログラミング言語でも、ライブラリを活用している
* 今一番話したい技術の話：Pythonの依存ライブラリ管理の仕組みと状況🍜
* 馴染みのある言語と比べて楽しんでいただければ

おことわり：nikkieのスタンス
--------------------------------------------------

* 本トークは小言を言っているように聞こえるかも
* 私はPythonが好き。手に馴染むし、これからも使い続けるだろうし、 **改善提案もしていく**

.. include:: one-obvious-way.rst.txt

.. include:: virtual-environments.rst.txt

.. include:: tools-made-with-rust.rst.txt

.. include:: recommendation.rst.txt

まとめ：Pythonに依存ライブラリ管理ツールがたっくさんある話
================================================================================

* Pythonではプロジェクトごとに仮想環境を用意する
* Pythonでは **小さな機能を組合せられる** ゆえに、たっくさんのツールが登場
* Rust製のRyeからの学び。我が推しはHatch

.. 担当はshirabe

.. revealjs-break::
    :notitle:

.. list-table::
    :header-rows: 1

    * - 項目
      - 俺たち
      - Rye
      - Hatch
    * - インストールにPythonが
      - 必要（前提）
      - 不要
      - どちらでも
    * - Pythonを管理
      - しない
      - する
      - する
    * - ライブラリ（仮想環境）管理
      - する（人力）
      - する
      - する
    * - 仮想環境の再現
      - 手順が漏れうる
      - ばっちり
      - ゆるめ

One more thing
======================================================================

**自作** しました

shirabe
--------------------------------------------------

.. code-block:: shell

    % shirabe alpha .venv

* :file:`requirements.txt` 込みで仮想環境を作る
* `私がほしいPythonの仮想環境を作るツール shirabe を実験的に始めました🎵 <https://nikkie-ftnext.hatenablog.com/entry/release-shirabe-python-virtual-environment-builder-v0.1.0>`__

.. revealjs-break::
    :notitle:

.. list-table::
    :header-rows: 1

    * - 項目
      - Hatch
      - shirabe
    * - インストールにPythonが
      - どちらでも
      - 必要
    * - Pythonを管理
      - する
      - しない
    * - ライブラリ（仮想環境）管理
      - する（意識しない）
      - する（意識させる）
    * - 仮想環境の再現
      - ゆるめ
      - ばっちり

ご清聴ありがとうございました
--------------------------------------------------

したっけね〜👋

【再掲】小言のように聞こえたかもしれませんが、Pythonという言語が好きなので、改善提案もしていきます（shirabe💪）

.. include:: appendix.rst.txt

EOF
===
