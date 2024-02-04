from docutils.nodes import literal_block, section
from sphinx_new_tab_link import NewTabLinkHTMLTranslator
from sphinx_revealjs.writers import RevealjsSlideTranslator


class TweakedRevealjsSlideTranslator(
    RevealjsSlideTranslator,
    # To override starttag method to open link in new tab
    NewTabLinkHTMLTranslator,
):
    def visit_literal_block(self, node: literal_block):
        lang = node["language"]
        # add section id as data-id if it is exists
        if "data-id" in node:
            self.body.append(f"<pre data-id=\"{node['data-id']}\">")
        elif isinstance(node.parent, section) and len(node.parent["ids"]):
            self.body.append(f"<pre data-id=\"{node.parent['ids'][0]}\">")
        else:
            self.body.append("<pre>")
        self.body.append(f'<code data-trim data-noescape class="{lang}"')
        # use the emphasize-lines directive to create line for line animations
        if "data-line-numbers" in node:
            self.body.append(
                f" data-line-numbers=\"{node['data-line-numbers']}\""
            )
        # Tweak https://github.com/attakei/sphinx-revealjs/compare/master...ftnext:sphinx-revealjs:code-block-emphasize-lines
        elif highlight_args := node.get("highlight_args"):
            if "hl_lines" in highlight_args:
                highlight_lines = ",".join(
                    str(num) for num in highlight_args["hl_lines"]
                )
                self.body.append(f' data-line-numbers="{highlight_lines}"')
        # Tweak End
        else:
            # show line numbers
            if node["linenos"]:
                self.body.append(" data-line-numbers")
        if "data-ln-start-from" in node:
            self.body.append(
                f" data-ln-start-from=\"{node['data-ln-start-from']}\""
            )
            if "data-line-numbers" not in node:
                self.body.append(" data-line-numbers")
        self.body.append(">")


def setup(app):
    app.set_translator("revealjs", TweakedRevealjsSlideTranslator)
