import csv
import sys

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as inp, open(sys.argv[2], 'w') as out:
            fieldnames = ['date', 'retweet_Monthly']
            writer = csv.DictWriter(out, fieldnames=fieldnames)
            writer.writeheader()

            for line in inp:
                parts = line.split(',')
                date = parts[0][11:19]
                retweet_Monthly = parts[1].split('=')[1]
                retweet_Monthly = retweet_Monthly[:len(retweet_Monthly)-2]
                writer.writerow({'date': date, 'retweet_Monthly': retweet_Monthly})
