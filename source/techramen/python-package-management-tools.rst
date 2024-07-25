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

* :fab:`github` `@ftnext <https://github.com/ftnext>`__ sphinx-new-tab-link などなど

Pythonは使いますか？
--------------------------------------------------

実務でも🙋‍♂️ 趣味でも🙋‍♀️

今日の話は **Pythonのライブラリを管理** する話
--------------------------------------------------

* どんなプログラミング言語でも、ライブラリを活用している
* 今一番話したい技術の話：Pythonの依存ライブラリ管理の仕組みと状況🍜
* 馴染みのある言語と比べて楽しんでいただければ

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

ご清聴ありがとうございました
--------------------------------------------------

したっけね〜👋
