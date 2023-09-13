CLEAN_TIME = 10
def solution(book_time):
    time = [0] * 1500
    book_time.sort()
    for bk in book_time:
        sh, sm = map(int, bk[0].split(":"))
        eh, em = map(int, bk[1].split(":"))
        start = sh * 60 + sm
        end = eh * 60 + em
        for minute in range(start, end + CLEAN_TIME):
            time[minute] += 1
    return max(time)