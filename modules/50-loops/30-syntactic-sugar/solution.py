def build_progress_bar(completed: int, total: int) -> str:
    index = 0
    result = ""

    while index < total:
        if index < completed:
            result += "#"
        else:
            result += "-"
        index += 1

    return result
