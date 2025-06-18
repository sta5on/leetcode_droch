lists = [[1,4,5],[1,3,4],[2,6]]

def mergeKLists(lists):
    merged = sorted(lists[0] + lists[1] + lists[2])
    return merged