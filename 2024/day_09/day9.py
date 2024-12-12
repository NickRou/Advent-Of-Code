class Utils:
    @staticmethod
    def parse_input(filename):
        with open(filename) as f:
            lines = f.read().splitlines()
        f.close()
        
        return lines



if __name__ == '__main__':
    pass
