from core.example import RockPaperScissors
import asyncio

async def main():
    rps = RockPaperScissors(3)

    turn_result = ""

    while "game" not in turn_result:
        turn_result = rps.make_a_turn(input())
        print(turn_result)


if __name__ == "__main__":
    asyncio.run(main())