from solution import normalize_filename


def test():
    assert normalize_filename("my photo.png") == "my_photo.png"
    assert normalize_filename("final report.pdf") == "final_report.pdf"
    assert normalize_filename("already_ready.txt") == "already_ready.txt"
    assert normalize_filename("two  spaces.txt") == "two__spaces.txt"
