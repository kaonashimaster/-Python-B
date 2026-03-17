'''
作成日: 2026/03/17
作成者: 相坂尚成
'''
#インポート

#グローバル変数宣言

#関数宣言
def go_dungeon(player_name):
    print(f"{player_name}はダンジョンに到着した")
    print(f"{player_name}はダンジョンを制覇した")
    defeated_monsters = 5
    return defeated_monsters

def main():
    player_name = input("プレイヤー名を入力してください> ")

    print("***Puzzle & Monsters***")
    
    go_dungeon(player_name)

    print("***GAME CLEARED!!***")

    print("倒したモンスター数=", go_dungeon(player_name))
#main関数呼び出し
main()