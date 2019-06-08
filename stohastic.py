import random, math

class Customer:
    def __init__(self, count, y, time_spent_to_process_this_customer):
        self.count = count  # номер человека
        self.y = y # время, через которое он придет
        self.time_when_customer_will_arrive = 0 #время, в которое он придет
        self.time_spent_to_process_this_customer = time_spent_to_process_this_customer # время на обработку этого человека


def exprand(lambdr):
    return -math.log(1.0 - random.random()) / lambdr


def getNext(count, lambd,nu):
    # Устанавливаем номер человека
    # время, через котрое он придет
    # и время, которое требуется на его обработку
    customer = Customer(count, exprand(1/lambd), exprand(1/nu))
    return customer


# Устанавливаем параметры
lambda_ = 5 # интенсивность
nu = 5 #пропускная способность
number_of_handlers = 1 # кол-во обработчиков
random.seed(42)

# Генерируем приходящих людей
list_of_customers = []

NUMBER_OF_STEPS = 50*1 # общее количество шагов == времени
lost_time = NUMBER_OF_STEPS  # оставшееся количество шагов == время для генерации

count = 0
while (lost_time > 0):
    count += 1
    customer = getNext(count, lambda_, nu)
    lost_time -= customer.y
    customer.time_when_customer_will_arrive = NUMBER_OF_STEPS - lost_time
    list_of_customers.append(customer)

print(len(list_of_customers))
for customer in list_of_customers:
    print(customer.time_when_customer_will_arrive)

# Обработчик
class Handler:
    

