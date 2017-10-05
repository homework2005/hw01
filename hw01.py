class seating:
    def __init__(self , filename):
        self.seat = self.read_file(filename)
        self.index = 0
        
    @staticmethod 
    def read_file(filename):
        try :
            with open(filename , 'r') as f:
                seat = [i.rstrip('\n').split(' ') for i in f]
                return seat
        except:
            print('file open failed')
            return None

    def cal_column(self):
        return len(self.seat)

    def search_seat(self , x , y):
        return self.seat[x][y]

    def replacement(self , a , b):
        for i in range(0 , len(self.seat) , 1):
            for j in range(0 , len(self.seat[i]) , 1):
                if self.seat[i][j] == a:
                    self.seat[i][j] = b
                    return True
        return False

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            element = self.seat[self.index]
            self.index += 1
            return element
        except IndexError:
            raise StopIteration
                    
def main():

    a = seating('input.txt')

    print('original seat :' , '\n'.join([str(i) for i in a]),sep='\n')
    print('There are %d column' % (a.cal_column()))
    print(u'第三排第二列 : ' , a.search_seat(1 , 2))
    print(u'第四排第一列 : ' , a.search_seat(0 , 3))
    print(u'第五排第三列 : ' , a.search_seat(2 , 4))

    if a.replacement('Jack' , 'Zhangsan'):
        print('Replace Jack with Zhangsan')
    if a.replacement('Tim' , 'Lisi'):
        print('Replace Tim with Lisi')
    if a.replacement('Will' , 'Wangwu'):
        print('Replace Will with Wangwu')

    print('After replacement :' , '\n'.join([str(i) for i in a]),sep='\n')
    

if __name__ == '__main__':
    main()
