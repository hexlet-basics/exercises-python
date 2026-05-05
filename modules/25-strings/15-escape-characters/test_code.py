from hexlet.test import expect_output


def test(capsys):
    expected = 'Для разделения строк используйте "\\n"\nПример: print("строка1\\nстрока2")'
    expect_output(capsys, expected)
