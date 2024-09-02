#!/usr/bin/env bash
set -euo pipefail

# Example: venv/lib/python3.12/site-packages/sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4/plugin/
revealjs_plugin_dir=$1

tempdir=$(mktemp -d)

curl -s -L https://github.com/Martinomagnifico/reveal.js-copycode/archive/refs/tags/v1.2.0.zip > "${tempdir}/copycode.zip"
unzip -q "${tempdir}/copycode.zip" -d "${tempdir}" 
mv "${tempdir}/reveal.js-copycode-1.2.0/plugin/copycode" "${revealjs_plugin_dir}"

rm -rf "${tempdir}"
