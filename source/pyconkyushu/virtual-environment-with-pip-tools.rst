======================================================================
venvによるPython開発環境の管理をpip-toolsでアップデートする提案
======================================================================

venvによるPython開発環境の管理を **pip-tools** でアップデートする提案
======================================================================

〜Ryeのソースリーディングより〜

:Event: PyCon Kyushu 2024 KAGOSHIMA
:Presented: 2024/05/24 nikkie

お前、誰よ
======================================================================

* nikkie ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続555日突破
* ソフトウェアエンジニアリングで突破するデータサイエンティスト（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* Python歴は6年。PyConで登壇多数

.. image:: ../_static/uzabase-white-logo.png

2022年以来ですね
--------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2022_slides/pyconk_kumamoto/revisit_python_from_statements.html"
        title="文に立ち返ってPython再入門"></iframe>

`アーカイブ動画 <https://youtu.be/jNbuQ-maCts?si=0z1OV8RCh8ih3G75>`__

皆さんのことを教えてください
======================================================================

簡単なアンケートにご協力ください🙏

副題 〜**Rye** のソースリーディングより〜
--------------------------------------------------

* 「Rye」を聞いたことがある🙋‍♂️
* Ryeを試した or 使っている🙋‍♀️
* Ryeのソースコードを少しでも覗いた🙋

**pip-tools** でアップデートする提案
--------------------------------------------------

* 「pip-tools」と聞いてピンと来る🙋‍♂️
* pip-toolsを使っている🙋‍♀️

存在感を増すRye
--------------------------------------------------

* 中身を理解しようとRust実装を覗き始めた（2024年1月）
* **仮想環境のパッケージ管理に活かせる要素** が見つかりました。共有します
* ⚠️Ryeの採用については発表の範囲外。廊下で話しましょう！

おことわり
--------------------------------------------------

* 全Python使いが知るべきとは思っていないので「上級」
* 仮想環境という題材はありふれているかもしれませんが、本トークは **掘り下げ** ます
* **macOS** で動作検証しています

3部構成でお届けします
--------------------------------------------------

1. **Pythonのパッケージ管理の基本をおさえる**
2. pip-toolsの提案
3. Ryeの依存パッケージ管理の実装紹介

.. include:: package-management-basic.rst.txt

venvによるPython開発環境の管理をpip-toolsでアップデートする提案
----------------------------------------------------------------------

1. Pythonのパッケージ管理の基本をおさえる
2. **pip-toolsの提案**
3. Ryeの依存パッケージ管理の実装紹介

.. include:: pip-tools-proposal.rst.txt

venvによるPython開発環境の管理をpip-toolsでアップデートする提案
----------------------------------------------------------------------

1. Pythonのパッケージ管理の基本をおさえる
2. pip-toolsの提案
3. **Ryeの依存パッケージ管理の実装紹介**

.. include:: rye-source-reading.rst.txt

まとめ🌯 venvによるPython開発環境の管理をpip-toolsでアップデートする提案
================================================================================

* 仮想環境 + ``pip freeze`` にツラさを感じている方（＝過去の私）へ
* 開発者はdirectな依存パッケージを指定。**pip-toolsがtransitiveな依存を管理**

ご清聴ありがとうございました
--------------------------------------------------

待ってます お話ししましょう *廊下* にて

Appendix
======================================================================

本編に盛り込めなかったコンテンツ

注目を集めるRye
--------------------------------------------------

* Twitter ``from:@voluntas Rye``
* methaneさん `ryeをpyenvのように使う <https://methane.hatenablog.jp/entry/2024/01/31/rye%E3%82%92pyenv%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E4%BD%BF%E3%81%86>`__

PyCon APAC 2023とRye
--------------------------------------------------

- `Pythonでのパッケージング：エコシステムの理解と現場での活用 <https://2023-apac.pycon.jp/timetable?id=BLGBSE>`__ (slide=41)
- `Comparison of Packaging Tools in 2023 <https://2023-apac.pycon.jp/timetable?id=XEGZUD>`__ (slide=31, 32)

nikkieとRye、試行錯誤録
--------------------------------------------------

* `Ryeのworkspaceで複数のパッケージを同時に開発している時に、workspaceのルートでmypyを流す（error: Duplicate module named "..."を--explicit-package-basesで解消） <https://nikkie-ftnext.hatenablog.com/entry/run-mypy-rye-workspace-root-with-explicit-package-bases>`__
* `Ryeのworkspaceで複数のパッケージを同時に開発している時に、workspaceのルートでpytestを流す（ModuleNotFoundErrorを--import-mode importlibで解消） <https://nikkie-ftnext.hatenablog.com/entry/run-pytest-rye-workspace-root-with-import-mode-importlib>`__
* `続・Ryeのworkspaceで複数のパッケージを同時に開発している時に、workspaceのルートでmypyを流す（strictモードで流すための対応案） <https://nikkie-ftnext.hatenablog.com/entry/run-strict-mypy-rye-workspace-root-with-unique-name-test-modules>`__

nikkieと仮想環境
--------------------------------------------------

* `Pythonの仮想環境、最近は .venv という名前で作っています <https://nikkie-ftnext.hatenablog.com/entry/python-venv-directory-name-202404>`__
* `Pythonのvenvの--upgrade-depsオプションは、どこから来てどこへ行くのか <https://nikkie-ftnext.hatenablog.com/entry/python-venv-upgrade-deps-option>`__

拙ブログより
--------------------------------------------------

* **pipxがめっちゃいいぞ！！** `Pythonスクリプトの未来。pipxが部分的にサポートしたInline script metadata（PEP 723）を触る <https://nikkie-ftnext.hatenablog.com/entry/henry-schreiner-pipx-supports-pep723-dependencies-metadata>`__
* `uvお試し記：uv venvで作った仮想環境でpip installしてはいけません。uv pip installしましょう <https://nikkie-ftnext.hatenablog.com/entry/uv-first-trial-different-implementation-venv>`__

EOF
======================================================================
