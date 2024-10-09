import pandas as pd
import time

CURRENT_TIME:int = 0
CURRENT_ID:int = 1
CPUS:int = 1
QUANTUM:int = 1
# DISPLAY_AS_A_TABLE:bool = False

# header = f"|{"Nome_do_processo":^20} | {"Tempo_de_execução":^20} | {"Tempo_de_chegada":^20} | {"Prioridade":^20}| {"Status":^20} |"
# print(header)
# print(f"{"-"*len(header)}")
# for process in processes:
#     print(f"|{process.name:^20} | {process.burst_time:^20} | {process.arrival_time:^20} | {process.priority:^20}| {process.status:^20} |")


class Process:
    """
    Representa um processo em um sistema operacional.

    Atributos:
        name (str): O nome do processo.
        arrival_time (int): O tempo de chegada do processo.
        burst_time (int): O tempo de execução do processo.
        priority (int): A prioridade do processo.
        waiting_time (int, opcional): O tempo de espera do processo. Padrão é 0.
        turnaround_time (int, opcional): O tempo de retorno do processo. Padrão é 0.
    """

    def __init__(self, name: str, arrival_time: int, burst_time: int, priority: int, waiting_time: int = 0, turnaround_time: int = 0):
        self.id = -1
        self.name = name
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.end_time = None
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = waiting_time
        self.status = "Not arrived"
        self.runned_this_time = False

    @property
    def turnaround_time(self):
        """
        Calcula o tempo de retorno do processo.

        Retorna:
            int: O tempo de retorno do processo.
        """
        if self.end_time is None:
            return None
        else:
            return self.end_time - self.arrival_time

    def arrive(self, display_priority=False):
        """
        Define o status do processo como "Pronto" e atribui um id único.

        Args:
            display_priority (bool, opcional): Se deve exibir a prioridade do processo. Padrão é False.
        """
        global CURRENT_ID
        if CURRENT_TIME >= self.arrival_time:
            self.status = "Ready"
            self.id = CURRENT_ID
            CURRENT_ID += 1
            if display_priority:
                print(f"{self.name} chegou com prioridade {self.priority}")
            else:
                print(f"{self.name} chegou")
        else:
            print(f"{self.name} ainda não chegou")

    def run(self, execution_time=1, display_priority=False):
        """
        Executes the process for a specified execution time.

        Args:
            execution_time (int, optional): The execution time of the process. Defaults to 1.
            display_priority (bool, optional): Whether to display the priority of the process. Defaults to False.
        """
        if display_priority:
            print(f"{CURRENT_TIME}     Executando {self.id} - {self.name} com prioridade {self.priority} por {execution_time} segundos, faltam {self.remaining_time} segundos")
        else:
            print(f"{CURRENT_TIME}     Executando {self.id} - {self.name} por {execution_time} segundos, faltam {self.remaining_time} segundos")
        time.sleep(execution_time)
        self.remaining_time -= execution_time
        if self.remaining_time == 0:
            self.end_time = CURRENT_TIME

    def wait(self):
        """
        Increases the waiting time of the process by 1.
        """
        self.waiting_time += 1

    def terminate(self):
        """
        Terminates the process and sets the end time and status.
        """
        self.end_time = CURRENT_TIME
        self.status = "Terminated"
        print(f"{self.name} terminou aos {CURRENT_TIME} segundos com um waiting time de {self.waiting_time} segundos")

    def __str__(self):
        return f"{self.name} {self.arrival_time} {self.burst_time} {self.priority} {self.id} {self.arrival_time} {self.end_time} {self.waiting_time} {self.turnaround_time} {self.status}"


def print_menu_w_priority() -> None:
    """
    Imprime as opções de menu para o algoritmo de escalonamento com prioridade.
    """
    print("1. First come first serve (FCFS)")
    print("2. Shortest job first (SJF)")
    print("3. Round Robin (RR)")
    print("4. Priority")
    print("0. Exit")

def print_menu_wo_priority() -> None:
        """
        Imprime as opções de menu para o algoritmo de escalonamento sem prioridade.
        """
        print("1. First come first serve (FCFS)")
        print("2. Shortest job first (SJF)")
        print("3. Round Robin (RR)")
        print("0. Exit")


with open("teste_escalonamento.txt", "r", encoding="UTF-8") as f:
    file_data = pd.read_csv(f, sep=" ")
    processes:list[Process] = []
    for i, process in file_data.iterrows():
        name:str = process["Nome_do_processo"]
        burst_time:int = process["Tempo_de_execução"]
        arrival_time:int = process["Tempo_de_chegada"]
        priority:int = process["Prioridade"]
        processes.append(Process(name=name, arrival_time=arrival_time, burst_time=burst_time, priority=priority))


print_menu_w_priority()
match input(f"Choose a number: "):
    case "0":
        exit()
    case "1":
        cpu_start_number = CPUS
        while [process for process in processes if process.status != "Terminated"]:
            for process in [process for process in processes if process.status == "Not arrived" and process.arrival_time <= CURRENT_TIME]:
                process.arrive()
            processes.sort(key=lambda x: x.arrival_time)
            for process in [process for process in processes if process.status == "Ready"]:
                if CPUS > 0:
                    process.status = "Running"
                    process.run()
                    CPUS -= 1
                else:
                    break
            for process in [process for process in processes if process.status == "Ready"]:
                process.wait()
            for process in [process for process in processes if process.status == "Running"]:
                if process.remaining_time == 0:
                    process.terminate()
                else:
                    process.status = "Ready"
            CPUS = cpu_start_number
            CURRENT_TIME += 1

        print(f"O tempo de espera médio foi de {sum([process.waiting_time for process in processes]) / len(processes)} segundos")

    case "2":
        cpu_start_number = CPUS
        while [process for process in processes if process.status != "Terminated"]:
            for process in [process for process in processes if process.status == "Not arrived" and process.arrival_time <= CURRENT_TIME]:
                process.arrive()
            processes.sort(key=lambda x: x.remaining_time)
            for process in [process for process in processes if process.status == "Ready"]:
                if CPUS > 0:
                    process.status = "Running"
                    process.run()
                    CPUS -= 1
                else:
                    break
            for process in [process for process in processes if process.status == "Ready"]:
                process.wait()
            for process in [process for process in processes if process.status == "Running"]:
                if process.remaining_time == 0:
                    process.terminate()
                else:
                    process.status = "Ready"
            CPUS = cpu_start_number
            CURRENT_TIME += 1

        print(f"O tempo de espera médio foi de {sum([process.waiting_time for process in processes]) / len(processes)} segundos") # exibe o tempo de espera médio

    case "3":
        QUANTUM = quantum = int(input("Enter the quantum: "))
        cpu_start_number = CPUS
        while [process for process in processes if process.status != "Terminated"]:
            quantum = QUANTUM
            for process in [process for process in processes if process.status == "Not arrived" and process.arrival_time <= CURRENT_TIME]:
                process.arrive()
            if [process for process in processes if process.status == "Ready" and process.runned_this_time == False]:
                for process in [process for process in processes if process.status == "Ready" and process.runned_this_time == False]:
                    if CPUS > 0:
                        process.status = "Running"
                        if quantum > process.remaining_time:
                            quantum = process.remaining_time
                        process.run(execution_time=quantum)
                        process.runned_this_time = True
                        CPUS -= 1
                    else:
                        break
                for process in [process for process in processes if process.status == "Ready"]:
                    process.wait()
                for process in [process for process in processes if process.status == "Running"]:
                    if process.remaining_time == 0:
                        process.terminate()
                    else:
                        process.status = "Ready"
                CPUS = cpu_start_number
                CURRENT_TIME += quantum
            else:
                for process in [process for process in processes if process.status == "Ready"]:
                    process.runned_this_time = False
                CPUS = cpu_start_number
                CURRENT_TIME += quantum

        print(f"O tempo de espera médio foi de {sum([process.waiting_time for process in processes]) / len(processes)} segundos") # exibe o tempo de espera médio

    case "4":
        print_menu_wo_priority()
        match input(f"Choose a number: "):
            case "0":
                exit()
            case "1":
                cpu_start_number = CPUS
                while [process for process in processes if process.status != "Terminated"]:
                    for process in [process for process in processes if process.status == "Not arrived" and process.arrival_time <= CURRENT_TIME]:
                        process.arrive(display_priority=True)
                    high_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 2]
                    high_priority_processes.sort(key=lambda x: x.arrival_time)
                    medium_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 1]
                    medium_priority_processes.sort(key=lambda x: x.arrival_time)
                    low_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 0]
                    low_priority_processes.sort(key=lambda x: x.arrival_time)
                    while CPUS > 0:
                        if high_priority_processes:
                            process = high_priority_processes[0]
                            process.status = "Running"
                            process.run(display_priority=True)
                            CPUS -= 1
                        elif medium_priority_processes:
                            process = medium_priority_processes[0]
                            process.status = "Running"
                            process.run(display_priority=True)
                            CPUS -= 1
                        elif low_priority_processes:
                            process = low_priority_processes[0]
                            process.status = "Running"
                            process.run(display_priority=True)
                            CPUS -= 1
                        else:
                            break
                    for process in [process for process in processes if process.status == "Ready"]:
                        process.wait()
                    for process in [process for process in processes if process.status == "Running"]:
                        if process.remaining_time == 0:
                            process.terminate()
                        else:
                            process.status = "Ready"
                    CPUS = cpu_start_number
                    CURRENT_TIME += 1

                print(f"O tempo de espera médio foi de {sum([process.waiting_time for process in processes]) / len(processes)} segundos")

            case "2":
                cpu_start_number = CPUS
                while [process for process in processes if process.status != "Terminated"]:
                    for process in [process for process in processes if process.status == "Not arrived" and process.arrival_time <= CURRENT_TIME]:
                        process.arrive(display_priority=True)
                    high_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 2]
                    high_priority_processes.sort(key=lambda x: x.remaining_time)
                    medium_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 1]
                    medium_priority_processes.sort(key=lambda x: x.remaining_time)
                    low_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 0]
                    low_priority_processes.sort(key=lambda x: x.remaining_time)
                    while CPUS > 0:
                        if high_priority_processes:
                            process = high_priority_processes[0]
                            process.status = "Running"
                            process.run(display_priority=True)
                            CPUS -= 1
                        elif medium_priority_processes:
                            process = medium_priority_processes[0]
                            process.status = "Running"
                            process.run(display_priority=True)
                            CPUS -= 1
                        elif low_priority_processes:
                            process = low_priority_processes[0]
                            process.status = "Running"
                            process.run(display_priority=True)
                            CPUS -= 1
                        else:
                            break
                    for process in [process for process in processes if process.status == "Ready"]:
                        process.wait()
                    for process in [process for process in processes if process.status == "Running"]:
                        if process.remaining_time == 0:
                            process.terminate()
                        else:
                            process.status = "Ready"
                    CPUS = cpu_start_number
                    CURRENT_TIME += 1
                print(f"O tempo de espera médio foi de {sum([process.waiting_time for process in processes]) / len(processes)} segundos")
            case "3":
                QUANTUM = quantum = int(input("Enter the quantum: "))
                cpu_start_number = CPUS
                while [process for process in processes if process.status != "Terminated"]:
                    quantum = QUANTUM
                    for process in [process for process in processes if process.status == "Not arrived" and process.arrival_time <= CURRENT_TIME]:
                        process.arrive(display_priority=True)
                    high_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 2]
                    medium_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 1]
                    low_priority_processes = [process for process in processes if process.status == "Ready" and process.priority == 0]
                    if [process for process in processes if process.status == "Ready" and process.runned_this_time == False]:
                        for process in [process for process in processes if process.status == "Ready" and process.runned_this_time == False]:
                            if CPUS > 0:
                                if high_priority_processes:
                                    process = high_priority_processes[0]
                                    process.status = "Running"
                                    if quantum > process.remaining_time:
                                        quantum = process.remaining_time
                                    process.run(execution_time=quantum, display_priority=True)
                                    process.runned_this_time = True
                                    CPUS -= 1
                                elif medium_priority_processes:
                                    process = medium_priority_processes[0]
                                    process.status = "Running"
                                    if quantum > process.remaining_time:
                                        quantum = process.remaining_time
                                    process.run(execution_time=quantum, display_priority=True)
                                    process.runned_this_time = True
                                    CPUS -= 1
                                elif low_priority_processes:
                                    process = low_priority_processes[0]
                                    process.status = "Running"
                                    if quantum > process.remaining_time:
                                        quantum = process.remaining_time
                                    process.run(execution_time=quantum, display_priority=True)
                                    process.runned_this_time = True
                                    CPUS -= 1
                                else:
                                    break
                            else:
                                break
                        for process in [process for process in processes if process.status == "Ready"]:
                            process.wait()
                        for process in [process for process in processes if process.status == "Running"]:
                            if process.remaining_time == 0:
                                process.terminate()
                            else:
                                process.status = "Ready" 
                        CPUS = cpu_start_number
                        CURRENT_TIME += quantum
                    else:
                        for process in [process for process in processes if process.status == "Ready"]:
                            process.runned_this_time = False
                        CPUS = cpu_start_number
                        CURRENT_TIME += quantum
                print(f"O tempo de espera médio foi de {sum([process.waiting_time for process in processes]) / len(processes)} segundos")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")
