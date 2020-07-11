def search(start, goal, graph):
    result = []
    generate([start], goal, result, graph)
    result.sort(key = lambda x : len(result))
    return result

def generate(path, goal, result, graph):
    state = path[-1]
    if state == goal:
        result.append(path)
    else:
        try:
            for i in graph[state]:
                if i not in path:
                    generate(path+[i], goal, result, graph)
        except Exception:
            pass

if __name__ == '__main__':
    Graph = {
        'A' : ['B', 'C', 'F'],
        'B' : ['C', 'F'],
        'C' : ['B','E', 'F']

    }
    print(search('A', 'F', Graph))