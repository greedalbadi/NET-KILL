
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
