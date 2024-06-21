def shortlist(singers):
    singer = {}
    for song in singers:
        print(song)
        if song in singer:
            singer[song] += 1
            print(singer)
        else:
            singer[song] = 1
            print(singer)

    max_count = max(singer.values())
    print(max_count)

    favourite_singer = sum(1 for count in singer.values() if count == max_count)
    return favourite_singer

def main():
    n= int(input().strip())
    array=list(map(int,input().strip().split()))
    array = array[:n]
    result = shortlist(array)
    print(result)
main()
