def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # بررسی ردیف‌ها، ستون‌ها و قطرها
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"بازیکن {current_player} - ردیف (0 تا 2): "))
            col = int(input(f"بازیکن {current_player} - ستون (0 تا 2): "))
        except ValueError:
            print("لطفاً عدد صحیح وارد کنید.")
            continue
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"🎉 بازیکن {current_player} برنده شد!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("😐 بازی مساوی شد!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("این خانه قبلاً پر شده. خانه دیگری را انتخاب کن.")
        else:
            print("مقدار وارد شده خارج از محدوده است.")

if __name__ == "__main__":
    main()
