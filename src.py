import socket
class Greedy_ddos:




    def load_headers(self):
        file = open("headers.txt")
        headers = file.read()
        file.close()
        return headers

    def load_agents(self):
        agents = open("agent.txt")
        agent_list = []
        for agent in agents.read().splitlines():
            agent_list.append(agent)
        return agent_list

def check_port(host, port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        port = int(port)
        server.connect_ex((host, port))
        server.close()
        return True
    except Exception as e:

        return False