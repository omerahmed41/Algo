'''
atm machine
'''

coins = [1, 2,  3, 5]
target = 120


def get_coins_numbers(coins, target):

    def dfs(target):
        if target < 1:
            return 0

        min_path = target
        for coin in coins:

            remaining = target - coin
            if remaining >= 0:
                min_path = min(target, 1 + dfs(remaining))
        return min_path

    return dfs(target)


# print(target, get_coins_numbers(coins, target))

def build_path(visited, res):
    path_dict = dict()
    path = []
    for key, val in visited.items():
        path_dict[val] = max(key, path_dict.get(val, 0))
    for i in range(res):
        print(path_dict[i+1] - path_dict[i])
        path.append(path_dict[i+1] - path_dict[i])
    return path_dict, path


def get_shortest_path(coins, target):

    visited = dict()
    visited[0] = 0

    def dfs(target):

        if target == 0:
            return 0

        min_path = target
        for coin in coins:
            remaining = target - coin
            if remaining >= 0:
                if remaining in visited:
                    min_path = min(min_path, 1 + visited[remaining])
                else:
                    _res = dfs(remaining)
                    min_path = min(min_path, 1 + _res)
                visited[target] = min_path

        return min_path

    res = dfs(target)
    return res, visited, build_path(visited, res)


if __name__ == "__main__":

    print(target, get_shortest_path(coins, target))
