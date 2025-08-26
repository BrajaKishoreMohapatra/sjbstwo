class Service:
    @staticmethod
    def echo(data):
        return data

    @staticmethod
    def get_algorithm_name(data):
        return data.get('algorithm', 'Algorithm name not provided')