import heapq

def _calculate_checksum(l: int, r: int, file_id: int) -> int:
    return (r*r-l*l+r+l)*file_id//2


def task_1(data: list[str]) -> int:
    data = list(map(int, data[0].strip()))
    ii, n = 2, len(data)
    jj = n-1 if n%2 == 1 else n-2
    result = 0
    pp = data[0]
    file_ii_id, file_jj_id = 1, n//2+n%1
    l_blocks, r_blocks = data[ii-1], data[jj]
    while ii<jj:
        if r_blocks >= l_blocks:
            r_blocks -= l_blocks
            result += _calculate_checksum(pp, pp+l_blocks-1, file_jj_id)
            pp += l_blocks
            result += _calculate_checksum(pp, pp+data[ii]-1, file_ii_id)
            pp += data[ii]
            ii += 2
            l_blocks = data[ii-1]
            file_ii_id += 1
            if not r_blocks:
                jj -= 2
                r_blocks = data[jj]
                file_jj_id -= 1
        else:
            l_blocks -= r_blocks
            result += _calculate_checksum(pp, pp+r_blocks-1, file_jj_id)
            pp += r_blocks
            jj -= 2
            r_blocks = data[jj]
            file_jj_id -= 1
    if r_blocks:
        result += _calculate_checksum(pp, pp+r_blocks-1, file_jj_id)
    return result

        
def task_2(data: list[str]) -> int:
    data = list(map(int, data[0].strip()))
    n = len(data)
    blanks = [[] for _ in range(10)]
    p = data[0]
    for ii in range(1, n, 2):
        if data[ii]:
            heapq.heappush(blanks[data[ii]], p)
        p += data[ii] + data[ii+1]
    
    def _get_blank_size(size_: int, min_p: int) -> int:
        min_ii = 0
        for ii in range(size_, 10):
            if blanks[ii] and blanks[ii][0] < min_p:
                min_p = blanks[ii][0]
                min_ii = ii
        return min_ii
                
    result = 0
    jj = n-1 if n%2 == 1 else n-2
    p_jj = p - data[jj]
    file_id = n//2+n%1
    while jj > 0:
        size_ = data[jj]
        blank = _get_blank_size(size_, p_jj)
        if blank:
            p = heapq.heappop(blanks[blank])
            result += _calculate_checksum(p, p+size_-1, file_id)
            left_size = blank - size_
            if left_size:
                heapq.heappush(blanks[left_size], p+size_)
        else:
            result += _calculate_checksum(p_jj, p_jj+size_-1, file_id)
        p_jj -= data[jj-1] + data[jj-2]
        jj -= 2
        file_id -= 1

    return result


if __name__ == "__main__":
    # with open("2024/data/example_09.txt", "r", encoding="utf-8") as _file:
    with open("2024/data/input_09.txt", "r", encoding="utf-8") as _file:
        data_ = _file.readlines()
        # print(task_1(data_))
        print(task_2(data_))
