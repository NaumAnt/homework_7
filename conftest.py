from zipfile import ZipFile

import pytest

@pytest.fixture(scope="session")
def create_archive_file():
    with ZipFile("files/archive.zip", "w") as archive:
        archive.write("files/import_empl_csv.csv", arcname='user_list.csv')
        archive.write("files/import_empl_xlsx.xlsx", arcname='user_list_for_xlsx.xlsx')
        archive.write("files/TestPDF.pdf", arcname='pdf_list.pdf')
    yield "files/archive.zip"
