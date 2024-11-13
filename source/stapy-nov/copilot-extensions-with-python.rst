======================================================================
PythonでもGitHub Copilot Extensions作れるもん！
======================================================================

PythonでもGitHub Copilot Extensions作れるもん！
======================================================================

:Event: みんなのPython勉強会#110 LT
:Presented: 2024/11/14 nikkie

お前、誰よ
======================================================================

* nikkie @ Copilotを馬車馬のように働かせ隊
* 機械学習エンジニア・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `みんなのPython勉強会 <https://startpython.connpass.com/>`__ スタッフ・4代目LT王子

.. image:: ../_static/uzabase-white-logo.png

GitHub Copilot Extensionsって、何よ
======================================================================

聞いたことありますか？🙋‍♂️

まず GitHub Copilot
--------------------------------------------------

**AI ペア プログラマー**

`GitHub Copilot とは何ですか? <https://docs.github.com/ja/copilot/about-github-copilot/what-is-github-copilot>`__
------------------------------------------------------------------------------------------------------------------------------------------------------

    GitHub Copilot は AI コーディング アシスタントであり、コードをより速く楽に記述できるため、問題解決とコラボレーションにより多くのエネルギーを集中できます。

様々な機能を搭載
--------------------------------------------------

:コード補完: 続くコードを提案してくれる。採用して少し直すだけ
:チャット: ChatGPTがVS Codeに住んでいるイメージ。色々聞けちゃう

ほかにもまだまだ！ なお進化中！

Copilot 棲息場所
--------------------------------------------------

課金して有効にすると

* VS Code（`拡張 <https://marketplace.visualstudio.com/items?itemName=GitHub.copilot>`__ をインストール）
* ブラウザで閲覧している GitHub の中 (github.com)

ご参考
--------------------------------------------------

.. raw:: html

    <iframe class="speakerdeck-iframe" style="border: 0px; background: rgba(0, 0, 0, 0.1) padding-box; margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" frameborder="0" src="https://speakerdeck.com/player/21bcfa0ac76a426e8b39ce92884a9f2a?slide=1" title="GitHub Copilot Tips and Tricks" allowfullscreen="true" data-ratio="1.7777777777777777"></iframe>

GitHub Copilot **Extensions**
======================================================================

Extension＝拡張

拡張、2つの方向性
--------------------------------------------------

:VS Code チャット拡張機能: VS Code拡張としてCopilot Chatを拡張できる（@する先の *エージェント*）
:GitHub Copilot Extensions: エージェントを作れる。このLTの本題

`Copilot 拡張機能の構築について <https://docs.github.com/ja/copilot/building-copilot-extensions/about-building-copilot-extensions>`__

GitHub Copilot Extensions
--------------------------------------------------

* GitHub Copilotをカスタマイズして、 **独自のエージェント** （Copilot Chatの相手）を作れる
* GitHubが用意する ``/chat/completions`` のエンドポイントを使える
* 例えば特定のリポジトリでRAGをするエージェント（プライベートのコードベースで）

服部さんの発表で知りました
--------------------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/UKpbIv0_J4A?si=DgWvs__rNEf6PMAj&amp;start=1364" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

実装例
--------------------------------------------------

* https://github.com/copilot-extensions
* Node.js, TypeScript
* Go

**Python** でもGitHub Copilot Extensions作れるもん！
======================================================================

得意なPythonを使いたい...！
--------------------------------------------------

* Hello worldにあたる `blackbeard-extension <https://github.com/copilot-extensions/blackbeard-extension>`__
* 海賊黒ひげとしてChatに応じる（※ONE PIECEではない）
* Node.jsによる実装

blackbeard-extension (Node.js) 抜粋
--------------------------------------------------

.. code-block:: javascript

  // https://github.com/copilot-extensions/blackbeard-extension/blob/11b5a9abaec14f57ee1c92350bf64553411deb02/index.js#L7-L48
  app.post("/", express.json(), async (req, res) => {
    const payload = req.body;
    const messages = payload.messages;
    messages.unshift({
      role: "system", content: "You are a helpful assistant that replies to user messages as if you were the Blackbeard Pirate.",
    });
    // Chatのユーザの入力にシステムプロンプトを加え、LLMに返答を生成させる
    const copilotLLMResponse = await fetch(
      "https://api.githubcopilot.com/chat/completions",
      // 省略
    )
    Readable.from(copilotLLMResponse.body).pipe(res);
  })

Pythonでもできました✌️（FastAPI❤️）
--------------------------------------------------

.. code-block:: python

    # https://github.com/ftnext/blackbeard-extension-python/blob/56ae295c54e2241645382a8a027a81316072b43b/app.py#L10-L40
    @app.post("/")
    async def stream(request: Request, x_github_token: str = Header(None)):
        payload = await request.json()
        messages = payload["messages"]
        messages.insert(
            0, {"role": "system", "content": "You are a helpful assistant that replies to user messages as if you were the Blackbeard Pirate."})

        def pass_generator():
            with httpx.stream(
                "POST", "https://api.githubcopilot.com/chat/completions", headers=headers, json=data,
            ) as response:
                # response.iter_lines() を yield

        return StreamingResponse(pass_generator(), media_type="text/event-stream")

簡単に動かせます！
--------------------------------------------------

Demo https://github.com/ftnext/blackbeard-extension-python

まとめ🌯 PythonでもGitHub Copilot Extensions作れるもん！
======================================================================

* Copilot Chatのエージェントを作れるGitHub Copilot Extensions
* **海賊黒ひげ拡張をPythonで実装** してみました
* OpenAIのGPTsのようなものをプログラミングで作っている感覚でとってもワクワク

ご清聴ありがとうございました
--------------------------------------------------

`blackbeard-extension-python <https://github.com/ftnext/blackbeard-extension-python>`__ お試しあれ！

☠️ゼハハハハ☠️
