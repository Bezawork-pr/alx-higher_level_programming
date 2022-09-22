#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    listfromhidden = dir(hidden_4)
    result = []
    count = 0
    for i in listfromhidden:
        for e in i:
            if e == "_":
                break
            else:
                result.append(i)
                break
    for e in result:
        print("{}".format(result[count]))
        count += 1
