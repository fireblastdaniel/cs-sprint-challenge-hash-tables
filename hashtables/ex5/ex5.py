# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    f_dict = {}
    result = []
    # Your code here
    for f in files:
        temp = f.split('/')
        if temp[-1] in f_dict:
            f_dict[temp[-1]].append(f)
        else:
            f_dict[temp[-1]] = [f]

    for q in queries:
        if q in f_dict:
            result += f_dict[q]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
