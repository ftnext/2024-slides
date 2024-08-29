:ogp_title: （ドラフト版）ライブラリ開発者に贈る「ロギングで NullHandler 以外はいけません」
:ogp_event_name: pyconshizu
:ogp_slide_name: logging-with-nullhandler
:ogp_description: PyCon mini Shizuoka 2024
:ogp_image_name: pyconshizu

.. _ライブラリのためのロギングの設定: https://docs.python.org/ja/3/howto/logging.html#configuring-logging-for-a-library
.. _ライブラリ内でロガーに NullHandler 以外のハンドラーを追加する: https://docs.python.org/ja/3/howto/logging-cookbook.html#adding-handlers-other-than-nullhandler-to-a-logger-in-a-library
.. _Logger.setLevel: https://docs.python.org/ja/3/library/logging.html#logging.Logger.setLevel

.. TODO 公式ドキュメントへのリンクを示すemojiを導入

======================================================================
ライブラリ開発者に贈る「ロギングで ``NullHandler`` 以外はいけません」
======================================================================

ライブラリ開発者に贈る「ロギングで ``NullHandler`` 以外はいけません」
======================================================================

ドラフト版

:Event: PyCon mini Shizuoka 2024（**延期**）
:Presented: 2024/08/31 nikkie

お前、誰よ
======================================================================

* nikkie ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続650日突破
* 機械学習エンジニア・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* Python歴は6年。PyConで登壇多数

.. image:: ../_static/uzabase-white-logo.png

アンケート（何度でも挙げよう）
--------------------------------------------------

* ``logging.warning()`` や ``logging.error()`` したことある🙋‍♂️
* ``logging.basicConfig()`` したことある🙋‍♀️
* ``logging.getLogger()`` したことある🙋

本トークの対象者
--------------------------------------------------

* Pythonのloggingモジュール **触ったことがある**
* loggingモジュールの中身はよく分からなくて全然OK👌

皆さんに質問です
======================================================================

* あなたはPythonで ``import`` して使いたいコードを書いています（例：ライブラリ）
* その中で **ロギング** をしたいです
* どう実装しますか？

結論：「``NullHandler`` 以外はいけません」
--------------------------------------------------

.. literalinclude:: ../../samplecode/python-logging/conclusion.py
    :language: python
    :lines: 1-4

公式ドキュメント「`ライブラリのためのロギングの設定`_」

メッセージ（Takeaway）
--------------------------------------------------

* ライブラリ開発者は *ロガー* を用意し、 *何もしないハンドラ* を設定しよう
* アプリケーション開発者は *ルートロガー* を設定し、 *propagate* を利用してログを表示しよう

斜体はこのトークで解説します

Logging クックブックの「避けるべきパターン」の1つ
======================================================================

* `ライブラリ内でロガーに NullHandler 以外のハンドラーを追加する`_

    (略) ログ出力をカスタマイズするのはライブラリ開発者ではなく、アプリケーション開発者の責務です。

本トークの構成
--------------------------------------------------

1. ライブラリ開発者へ
2. アプリケーション開発者へ
3. 落ち穂拾い

.. おことわり？ 限定的

.. include:: library-logging.rst.txt

.. include:: application-logging.rst.txt
