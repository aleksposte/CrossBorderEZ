import zipfile
from io import BytesIO


def create_svg_zip(svg_content: str, filename: str) -> BytesIO:
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, "w") as zf:
        zf.writestr(filename, svg_content)
    memory_file.seek(0)
    return memory_file
