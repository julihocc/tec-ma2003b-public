from pathlib import Path
from typing import Iterable
import argparse
from pdfminer.high_level import extract_text


def find_pdfs(path: Path, recursive: bool = False) -> Iterable[Path]:
    if path.is_file():
        yield path
        return
    if not path.exists():
        return
    if recursive:
        for p in path.rglob("*.pdf"):
            yield p
    else:
        for p in path.glob("*.pdf"):
            yield p


def extract_to_path(pdf_path: Path, out_path: Path, force: bool = False) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not force:
        raise FileExistsError(
            f"Output file exists: {out_path} (use --force to overwrite)"
        )
    text = extract_text(str(pdf_path))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF file or all PDFs in a folder. By default saves a .txt next to each PDF."
    )
    parser.add_argument(
        "source",
        nargs="?",
        default="backup/ma2003b/Beamers/MA2003B_DrJonathanMontalvo_20250821.pdf",
        help="PDF file or directory containing PDFs (default: the beamers PDF in backup)",
    )
    parser.add_argument(
        "--outdir",
        "-o",
        help="Output directory to place extracted text files (overrides in-place)",
    )
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="Save the .txt file next to the original PDF (default)",
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="When source is a directory, process PDFs recursively",
    )
    parser.add_argument(
        "--force", "-f", action="store_true", help="Overwrite existing .txt files"
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    src = Path(args.source)
    if not src.exists():
        print(f"Source does not exist: {src}")
        return 2

    outdir = Path(args.outdir) if args.outdir else None

    processed = []
    for pdf in find_pdfs(src, recursive=args.recursive):
        if not pdf.suffix.lower() == ".pdf":
            if args.verbose:
                print(f"Skipping non-pdf: {pdf}")
            continue

        if outdir:
            target = outdir / (pdf.stem + ".txt")
        elif args.inplace or src.is_file():
            target = pdf.with_suffix(".txt")
        else:
            # default: place into build/ma2003b/beamers preserving filename
            target = Path("build/ma2003b/beamers") / (pdf.stem + ".txt")

        try:
            res = extract_to_path(pdf, target, force=args.force)
            processed.append(res)
            if args.verbose:
                print(f"Extracted: {pdf} -> {res}")
        except FileExistsError as e:
            print(e)
        except Exception as e:
            print(f"Error extracting {pdf}: {e}")

    if not processed:
        print("No PDFs processed.")
        return 1

    print(f"Processed {len(processed)} PDF(s). Last output: {processed[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
