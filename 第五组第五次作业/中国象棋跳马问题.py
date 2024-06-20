def knight_tour(n, start_x, start_y):
    # 方向数组表示马可以走的8个方向
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    # 棋盘初始化
    board = [[-1] * n for _ in range(n)]
    board[start_x][start_y] = 0  # 起始点设为0

    # 计数器，记录成功路径数
    success_count = [0]

    # 辅助函数，检查是否在棋盘内
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    # 回溯函数
    def backtrack(x, y, move_count):
        if move_count == n * n - 1:  # 如果走过了所有格子
            success_count[0] += 1
            print_board(board)
            return True

        # 尝试8个方向
        for move in moves:
            next_x = x + move[0]
            next_y = y + move[1]
            if is_valid(next_x, next_y):
                board[next_x][next_y] = move_count + 1
                if backtrack(next_x, next_y, move_count + 1):
                    return True
                board[next_x][next_y] = -1

        return False

    # 开始回溯
    backtrack(start_x, start_y, 0)

    # 输出成功路径数
    print(f"成功路径数: {success_count[0]}")

# 辅助函数，打印棋盘
def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end="\t")
        print()
    print()

# 示例调用
n = 5
start_x = 0
start_y = 0
knight_tour(n, start_x, start_y)
