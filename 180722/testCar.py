#Car 클래스 정의
class Car:
    def __init__(self):     #객체생성될때 실행됨(초기값주기)
        #initialize 초기화하다
        print('자동차생성')
        self.color = "red"
        self.wheel_size = 16
        self.displacement = 2000

    def forward(self):  #전진
        pass

    def backward(self):  #후진
        pass

    def turn_left(self):  #좌회전
        pass

    def turn_right(self):  #우회전
        pass

#Car 클래스 정의 종료
#Car 클래스의 인스턴스를 정의하고 사용하는 코드 (객체생성)
if __name__ == '__main__':
    my_car = Car()      #객체생성

    print(my_car.color)
    print(my_car.wheel_size)
    print(my_car.displacement)


    my_car.forward()
    my_car.backward()

