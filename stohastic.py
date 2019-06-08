import random, math

class Customer:
    def __init__(self, count, y, time_to_process_this_customer):
        self.count = count  # номер человека
        self.y = y # время, через которое он придет
        self.time_when_customer_will_arrive = 0 #время, в которое он придет
        self.time_to_process_this_customer = round(time_to_process_this_customer) + 1 # время на обработку этого человека (+1 временное решение того, что 0 требуется на процесс)


def exprand(lambdr):
    return -math.log(1.0 - random.random()) / lambdr


def get_next(count, lambd,nu):
    # Устанавливаем номер человека
    # время, через котрое он придет
    # и время, которое требуется на его обработку
    customer = Customer(count, exprand(1/lambd), exprand(1/nu))
    return customer


# Устанавливаем параметры
lambda_ = 1 # интенсивность
nu = 5 #пропускная способность
number_of_handlers = 2 # кол-во обработчиков
random.seed(42)

# Генерируем приходящих людей
list_of_customers = []

NUMBER_OF_STEPS = 50*1 # общее количество шагов == времени
lost_time = NUMBER_OF_STEPS  # оставшееся количество шагов == время для генерации

count = 0
while (lost_time > 0):
    count += 1
    customer = get_next(count, lambda_, nu)
    lost_time -= customer.y
    customer.time_when_customer_will_arrive = round(NUMBER_OF_STEPS - lost_time)
    list_of_customers.append(customer)

print("Number of customers:" + str(len(list_of_customers)))
for customer in list_of_customers:
    print("time_when_customer_will_arrive: "+str(customer.time_when_customer_will_arrive) + " and time_to_process_this_customer:" + str(customer.time_to_process_this_customer))

# Обработчик
class Handler:
    def __init__(self, id):
        self.customer = None
        self.id = id

    def process_customer(self):
        if (self.customer is not None):
            print("Id of handler:"+str(self.id))
            self.customer.time_to_process_this_customer -= 1
            print("Time left:" + str(self.customer.time_to_process_this_customer))
            if (self.customer.time_to_process_this_customer < 1):
                self.customer = None
                print("Processed!")


list_of_handlers = []
for i in range(number_of_handlers):
    list_of_handlers.append(Handler(i))

gone = 0
last_index = 0
for i in range(NUMBER_OF_STEPS):
    print("\nSTEP" + str(i))
    new_customer = None
    # достаем людей, которые пришли в данную секунду (а что, если несколько человек в одно время?)
    new_customers = [customer for customer in list_of_customers if customer.time_when_customer_will_arrive == i]
    print("New customer in current time: " + str(len(new_customers)))
    for customer in list_of_customers:
        if (customer.time_when_customer_will_arrive == i):
            new_customer = customer
            break
    

    # обрабатываем людей
    for handler in list_of_handlers:
        handler.process_customer()

    # если есть пустые кассы, то пихаем туда человека
    if (new_customer is not None):
        is_wait = True
        for handler in list_of_handlers:
            if handler.customer is None:
                print("New customer, time to process: " + str(new_customer.time_to_process_this_customer))
                handler.customer = new_customer
                is_wait = False
                break
        # иначе счетчик ушедших++
        if (is_wait):
            print("Gone!")
            gone += 1    
    # продолжаем

print(gone)
