# python3


def build_heap(data):
    swaps = []
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n// 2, -1, -1):

        smth=i
        right = 2*smth+2 
        left = 2*smth+1

        while True:
            index = smth
            if right < n and data[right] < data[index]:
                index = right
            if left < n and data[left] < data[index]:
                index=left

            if smth != index:
                swaps.append((smth, index))
                data[smth], data[index] = data[index], data[smth]
                smth = index
                right= 2*smth + 2
                left= 2*smth + 1
            
            else:
                break


    return swaps


def main():
    apainter = input()

    if "F" in apainter:
        path = './test/'
        file = input()
        folder = path + file
        if "a" not in file:
            try:
                with open(folder) as f:
                    n = int(f.readline())
                    data = list(map(int, f.readline().split()))
            except Exception as e:
                print("Kluda:(", str(e))
                return

        else:
            print("Kluda")

    if "I" in apainter:
        n = int(input())
        data = list(map(int, input().split()))

    # Check that data is assigned before use
    if 'data' not in locals():
        print("Kluda: data not assigned")
        return

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= n * 4

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
