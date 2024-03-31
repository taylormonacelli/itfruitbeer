import pathlib

import md_toc

from . import main2

__project_name__ = "itfruitbeer"


def main() -> int:
    rendered = main2.render_template("readme/readme.md.j2")
    outfile = pathlib.Path("README.md")
    outfile.write_text(rendered)
    toc = md_toc.build_toc(outfile)
    md_toc.write_string_on_file_between_markers(outfile, toc, "<!--TOC-->")

    scripts = [
        {
            "outfile": "script01.sh",
            "tmpl": "readme/script01/script.sh.j2",
        },
        {
            "outfile": "script02.sh",
            "tmpl": "readme/script02/script.sh.j2",
        },
        {
            "outfile": "script03.sh",
            "tmpl": "readme/script03/script.sh.j2",
        },
    ]

    for dct in scripts:
        rendered = main2.render_template(dct["tmpl"])
        outfile = pathlib.Path(dct["outfile"])
        outfile.write_text(rendered)

        if outfile.suffix == ".sh":
            outfile.chmod(0o755)

    return 0
