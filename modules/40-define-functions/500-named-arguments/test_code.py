import index


def test():
    assert index.trim_and_repeat('python') == 'python'
    assert index.trim_and_repeat('python', offset=4) == 'on'
    assert index.trim_and_repeat('python', repetitions=2) == 'pythonpython'
    assert index.trim_and_repeat('python', offset=4, repetitions=2) == 'onon'
