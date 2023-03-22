import sys
def take_input(producers, consumers):
    producer_price, producer_date = zip(*[map(int, inputs[i].split()) for i in range(1, producers + 1)])
    consumer_price, consumer_date = zip(*[map(int, inputs[j].split()) for j in range(producers + 1, producers + consumers + 1)])
    return producer_price, producer_date, consumer_price, consumer_date

def money_for_nothing(producers, consumers):
    producerprice, producerdate, consumerprice, consumerdate = take_input(producers,consumers)
    profit, new_profit = 0, 0
    for i1 in range(producers):
        for j1 in range(consumers):
            if consumerdate[j1] - producerdate[i1] > 0 and consumerprice[j1] - producerprice[i1] > 0:
                profit = (consumerprice[j1] - producerprice[i1]) * (consumerdate[j1] - producerdate[i1])
            if new_profit < profit:
                new_profit = profit
    return new_profit

inputs = sys.stdin.readlines()
producers, consumers = map(int, inputs[0].split())
print(money_for_nothing(producers, consumers))

    








































