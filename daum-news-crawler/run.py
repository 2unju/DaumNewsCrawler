from crawler import news
from arguments import get_args

from multiprocessing import Pool


def run_multiprocess(args):
    if args.category == "all":
        news_category = ["politics", "economic", "culture", "digital", "society"]
        pool = Pool(processes=args.num_process)
        pool.map(news, news_category)
        pool.close()
        pool.join()
    else:
        print("Multiprocessing is not supported for a single category")


def run_singleprocess(args):
    if args.category == "all":
        for category in ["politics", "economic", "culture", "digital", "society"]:
            news(category)
    else:
        news(args.category)


if __name__ == "__main__":
    args = get_args()
    if args.multiprocessing == "True":
        run_multiprocess(args)
    else:
        run_singleprocess(args)
