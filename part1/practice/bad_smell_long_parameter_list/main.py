# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, state):
        self.state = state
        self.speed = 1

    def move(self, direction):
        speed = self.unit_speed()
        if direction == 'UP':
            self.field.set_unit(x=self.coord_x, y=(self.coord_y + speed), unit=self)
        elif direction == 'DOUW':
            self.field.set_unit(x=self.coord_x, y=(self.coord_y - speed), unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=(self.coord_x - speed), y=self.coord_y, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(x=(self.coord_x + speed), y=self.coord_y, unit=self)

    def unit_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        return self.speed



    # def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):

        # if is_fly and crawl:
        #     raise ValueError('Рожденный ползать летать не должен!')
        #
        # if is_fly:
        #     speed *= 1.2
        #     if direction == 'UP':
        #         new_y = y_coord + speed
        #         new_x = x_coord
        #     elif direction == 'DOWN':
        #         new_y = y_coord - speed
        #         new_x = x_coord
        #     elif direction == 'LEFT':
        #         new_y = y_coord
        #         new_x = x_coord - speed
        #     elif direction == 'RIGTH':
        #         new_y = y_coord
        #         new_x = x_coord + speed
        # if crawl:
        #     speed *= 0.5
        #     if direction == 'UP':
        #         new_y = y_coord + speed
        #         new_x = x_coord
        #     elif direction == 'DOWN':
        #         new_y = y_coord - speed
        #         new_x = x_coord
        #     elif direction == 'LEFT':
        #         new_y = y_coord
        #         new_x = x_coord - speed
        #     elif direction == 'RIGTH':
        #         new_y = y_coord
        #         new_x = x_coord + speed
        #
        #     field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
