import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--multiprocessing', default=True)
    parser.add_argument('--num-process', default=5)
    parser.add_argument('--logger', default=True)
    parser.add_argument('--max-num', default=200000)
    parser.add_argument('--category', default="all",
                        choices=["all", "politics", "economic", "culture", "digital", "society"])

    args = parser.parse_args()
    return args
