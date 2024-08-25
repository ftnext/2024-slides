:ogp_title: （ドラフト版）ライブラリ開発者に贈る「ロギングで NullHandler 以外はいけません」
:ogp_event_name: pyconshizu
:ogp_slide_name: logging-with-nullhandler
:ogp_description: PyCon mini Shizuoka 2024
:ogp_image_name: pyconshizu

.. _ライブラリのためのロギングの設定: https://docs.python.org/ja/3/howto/logging.html#configuring-logging-for-a-library

======================================================================
ライブラリ開発者に贈る「ロギングで ``NullHandler`` 以外はいけません」
======================================================================

ドラフト版

:Event: PyCon mini Shizuoka 2024
:Presented: 2024/08/31 nikkie

お前、誰よ
======================================================================

.. 聴衆の想定など

皆さんに質問です
======================================================================

* あなたはPythonで再利用したいコードを書いています（例：ライブラリ）
* その中でロギングをしたいです
* どう実装しますか？

結論：「``NullHandler`` 以外はいけません」
--------------------------------------------------

.. code-block:: python

    import logging

    logger = logging.getLogger("mylib")
    logger.addHandler(logging.NullHandler())

公式ドキュメント「`ライブラリのためのロギングの設定`_」

このトークを通して
--------------------------------------------------

* 先のコード（``NullHandler`` 以外はいけません）を理解・納得してもらえたら嬉しいです
* 結論以外のコードがよくない理由も追って話します

Logging クックブックの「避けるべきパターン」の1つ
======================================================================

* `ライブラリ内でロガーに NullHandler 以外のハンドラーを追加する <https://docs.python.org/ja/3/howto/logging-cookbook.html#adding-handlers-other-than-nullhandler-to-a-logger-in-a-library>`__

    ハンドラーやフォーマッター、フィルターを追加してログ出力をカスタマイズするのはライブラリ開発者ではなく、アプリケーション開発者の責務です。

本トークの構成
--------------------------------------------------

1. ライブラリ開発者へ
2. アプリケーション開発者へ

.. include:: library-logging.rst.txt
