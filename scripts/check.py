"""Static checks: nav anchors resolve, local asset refs exist, no root-relative paths."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf8")
ids = set(re.findall(r'id="([^"]+)"', html))
errs = [f"missing anchor #{a}" for a in set(re.findall(r'href="#([^"]+)"', html)) if a not in ids]
errs += [f"root-relative path breaks on project pages: {m}" for m in re.findall(r'(?:src|href)="(/[^"/][^"]*)"', html)]
OPTIONAL = {"assets/me.jpeg"}  # images are optional; pages fall back to placeholders
for m in set(re.findall(r'src="(assets/[^"$]+)"', html)):
    if not (root / m).exists() and m not in OPTIONAL:
        errs.append(f"missing asset {m}")
print("\n".join(errs) or "OK: anchors, paths, assets"); sys.exit(1 if errs else 0)
