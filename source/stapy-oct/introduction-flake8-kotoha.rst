======================================================================
関数の引数の型ヒントをカイゼンするflake8 pluginを作りました！！
======================================================================

関数の引数の型ヒントをカイゼンするflake8 pluginを作りました！！
======================================================================

:Event: みんなのPython勉強会#109 LT
:Presented: 2024/10/17 nikkie

お前、誰よ
======================================================================

* nikkie ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続 **690** 日突破
* 機械学習エンジニア・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `みんなのPython勉強会 <https://startpython.connpass.com/>`__ スタッフ・4代目LT王子

.. image:: ../_static/uzabase-white-logo.png

型ヒント
======================================================================

書いている方🙋‍♂️

Python 3.5から型ヒントが書けるようになった
--------------------------------------------------

.. code-block:: python
    :caption: 文字列 name を受け取り、文字列を返す関数 greeting

    def greeting(name: str) -> str:
        return "Hello " + name
    
    greeting("stapy")  # 'Hello stapy'

型チェッカが使う
--------------------------------------------------

* Python処理系が実行するとき、型ヒントは無視
* 型チェッカ（例：mypy）で **型ヒントをチェック** する

.. code-block:: python

    # error: Argument 1 to "greeting" has incompatible type "int"; expected "str"  [arg-type]
    greeting(42)

実行時は無視されるとはいっても、書くと便利
--------------------------------------------------

* 処理系で実行する前に **エラーになることに気づける**
* 型チェッカではなく **人が読む前提** で型ヒントを書くことで情報量を増やせる

この型ヒントは、Python公式ドキュメントで推奨？ 非推奨？ クイズ！！！！
======================================================================

要素に1を加える関数の型ヒント
--------------------------------------------------

.. code-block:: python

    def plus_one(numbers: list[int]) -> list[int]:
        return [n + 1 for n in numbers]

    plus_one([1, 2, 3])  # [2, 3, 4]

Python公式ドキュメントで推奨？ 非推奨？

ヒント：引数の型ヒント
--------------------------------------------------

.. code-block:: python
    :emphasize-lines: 2

    def plus_one(
        numbers: list[int]
    ) -> list[int]:
        return [n + 1 for n in numbers]

Python公式ドキュメントで推奨？ 非推奨？

答え：非推奨🙅‍♀️！！
======================================================================

    Note that to annotate arguments, it is preferred to use an abstract collection type such as Sequence or Iterable rather than to use list or typing.List.

https://docs.python.org/ja/3/library/typing.html#typing.List

意訳
--------------------------------------------------

    関数の引数を型ヒントするとき、listよりもSequenceやIterableのような抽象コレクション型を使うのが好ましい

公式ドキュメントを元にした私の考え
--------------------------------------------------

.. code-block:: python
    :emphasize-lines: 1,4

    from collections.abc import Iterable

    def plus_one(
        numbers: Iterable[int]
    ) -> list[int]:
        return [n + 1 for n in numbers]

Iterable
--------------------------------------------------

* https://docs.python.org/ja/3/glossary.html#term-iterable
* **要素を1度に1つずつ返せる** オブジェクト（だから ``for`` と使える）
* ``list`` は（シーケンスであり）イテラブル

その引数の型ヒント、本当に ``list`` ですか？
--------------------------------------------------

* ``list`` を渡して呼び出してはいる
* **タプルを渡しても** 動く（``range`` やジェネレータでも。これらは皆イテラブル）
* 表したいのは「整数を要素としていて **forで回せる**」なのでは？

関数の引数の型ヒントをカイゼンするflake8 pluginを作りました！！
======================================================================

.. code-block:: shell
    
    $ pip install flake8-kotoha

https://pypi.org/project/flake8-kotoha/

.. _Flake8: https://flake8.pycqa.org/en/stable/

リンター `Flake8`_
--------------------------------------------------

* コードを実行せずに解析（＝静的解析）して、スタイルや問題を指摘
* プラグインを書けるので、「その引数の型ヒント、本当に ``list`` か」問うプラグインをこのたび実装

flake8-kotoha「引数の型ヒントをlistにしてはいけません」
------------------------------------------------------------

.. code-block:: shell

    $ flake8 example.py
    example.py:1:14: KTH101 Type hint with abstract type `collections.abc.Iterable` or `collections.abc.Sequence`, instead of concrete type `list`

なぜRuffでなくてFlake8？
------------------------------------------------------------

* Rust実装の高速なリンター兼フォーマッタ Ruff がFlake8・Black・isortなどを置き換えていっているように映る
* **Ruffにplugin機構が現時点でなさそう** だからです（あったらやりたいので情報求ム）

まとめ🌯 関数の引数の型ヒントをカイゼンするflake8 pluginを作りました！！
================================================================================

* 関数の引数に ``list`` を渡していたとしても、``list`` を使った型ヒントが好ましいとは限らない
* 自作した flake8-kotoha 「引数の型ヒントをlistにしてはいけません」

ご清聴ありがとうございました
--------------------------------------------------

Kaizen Type Hint💪
