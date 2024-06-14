"""

使用Python 3.9开发剪刀石头布游戏。
遵循PEP 8规范组织游戏的代码结构,提高可维护性。
将游戏逻辑、用户交互和结果判定分别封装在不同的函数或类中。
使用if语句和字符串方法验证用户输入是否为合法的游戏选择(剪刀/石头/布)。
使用while循环控制游戏进行多轮,直到用户主动退出。
利用random模块生成表示剪刀、石头、布的随机数,模拟电脑玩家的选择。
使用ANSI转义序列为游戏结果输出添加颜色,提升视觉效果。
使用pyfiglet等库生成炫酷的ASCII艺术字,作为游戏开始和结束的提示文本。
允许玩家通过命令行参数选择游戏难度,如"easy"、"hard"等,影响电脑随机策略的生成算法。
在本地JSON文件中存储用户的游戏胜负统计信息,持久化游戏记录。

"""

import random
import json
import os
import sys
import pyfiglet

# 定义游戏结果颜色
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m'
}

# 定义游戏结果
WIN = 1
LOSE = -1
DRAW = 0

# 定义游戏选项
OPTIONS = ['rock', 'scissors', 'paper']

# 定义游戏结果
RESULTS = {
    'rock': {
        'rock': DRAW,
        'scissors': WIN,
        'paper': LOSE
    },
    'scissors': {
        'rock': LOSE,
        'scissors': DRAW,
        'paper': WIN
    },
    'paper': {
        'rock': WIN,
        'scissors': LOSE,
        'paper': DRAW
    }
}

# 定义游戏难度
DIFFICULTY = {
    'easy': lambda: random.choice(OPTIONS),
    'hard': lambda: random.choice(OPTIONS + [random.choice(OPTIONS)])
}

def get_user_choice():
    """
    获取用户选择
    """
    while True:
        user_choice = input("Please choose (rock/scissors/paper): ")
        if user_choice.lower() in OPTIONS:
            return user_choice.lower()
        else:
            print("Invalid input. Please try again.")

def get_computer_choice(difficulty):
    """
    获取电脑选择
    """
    return DIFFICULTY[difficulty]()

def determine_result(user_choice, computer_choice):
    """
    判断游戏结果
    """
    result = RESULTS[user_choice][computer_choice]
    return result

def display_result(result):
    """
    显示游戏结果
    """
    if result == WIN:
        print(COLORS['GREEN'] + "You win!" + COLORS['END'])
    elif result == LOSE:
        print(COLORS['RED'] + "You lose!" + COLORS['END'])
    else:
        print("It's a draw!")

def play_game(difficulty):
    """
    开始游戏
    """
    print(pyfiglet.figlet_format("Rock Paper Scissors"))
    print("Welcome to Rock Paper Scissors!")
    print("Difficulty: " + difficulty)
    print("-----------------------------")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice(difficulty)
        result = determine_result(user_choice, computer_choice)
        display_result(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    difficulty = "easy"  # 默认游戏难度为easy
    if len(sys.argv) > 1:
        difficulty = sys.argv[1].lower()
        if difficulty not in DIFFICULTY:
            print("Invalid difficulty. Using default difficulty (easy).")

    play_game(difficulty)






