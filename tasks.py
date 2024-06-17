TASKS1 = [
    r'Найдите все значения корня $\sqrt[4]{-16}$.',
    r'Найдите все значения корня $\sqrt[4]{16}$.',
    r'Найдите все значения корня $\sqrt[3]{\frac{1}{8}}$.',
    r'Найдите все значения корня $\sqrt[3]{-8i}$.',
    r'Найдите все значения корня $\sqrt[4]{1-2i}$.'
]

TASKS2 = [
    r'Найдите $\frac{\partial f}{\partial z}$, если $f(z)= z\sin{|z|^2}$',
    r'Найдите $\frac{\partial f}{\partial \overline{z}}$, если $f(z)= ze^{|z|^2}$',
    r'Найдите $\frac{\partial f}{\partial \overline{z}}$, если $f(z)= x + y + ixy$'

]

TASKS3 = [
    r'Вычислите интегралы $\displaystyle\int_{AB}(4z^3 +1)\overline{z}dz$;\quad$\displaystyle\int_{AB}(4z^3 +1)\overline{z}|dz|;$\quad$AB$ - отрезок $z_A = 1, z_B = i$.',
    r'Вычислите интегралы $\displaystyle\int_{AB}(2z+1)\overline{z}dz$;\quad$\displaystyle\int_{AB}(2z+1)\overline{z}|dz|;$\quad$AB = \{z:y = x^3, z_A = 0, z_B = 1+i\}$.',
    r'Вычислите интегралы $\displaystyle\int_{AB}z\,\mathrm{Im} \, z^2 \, dz$;\quad$\displaystyle\int_{AB}z\,\mathrm{Im} \, z^2 \, dz;$\quad$AB$ - отрезок $z_A = 0, z_B = 1+i$.',
    r'Вычислите интегралы $\displaystyle\int_{AB}(4z^3 +1)\overline{z}dz$;\quad$\displaystyle\int_{AB}(4z^3 +1)\overline{z}|dz|;$\quad$AB$ - отрезок $z_A = 1, z_B = i$.'
]

TASKS4 = [
    r'Найдите область сходимости $\sum_{n=1}^{\infty} \left(1 + \frac{n}{n+i} \cos \frac{n \pi}{2} \right) \cdot z^{n^2}$',
    r'Найдите область сходимости $\sum_{n=1}^{\infty}\frac{n}{n+1}\sin^2{\frac{n \pi}{4}}\cdot z^n$'
]

TASKS5 = [
    r'Найдите все изолированные особые точки функции $f(z) = \frac{\sin{\pi z}}{(z-1)^3}$ и определите их тип.',
    r'Найдите все изолированные особые точки функции $f(z) = \frac{1}{1-\cos{z}}$ и определите их тип.',
    r'Найдите все изолированные особые точки функции $f(z) = \frac{1-\cos{z}}{z\sin^2{z}}$ и определите их тип.'
]

TASKS6 = [
    r'Вычислить интеграл, используя формулу Коши-Грина: $\displaystyle\oint\limits_{|z|=1} \overline{z}z^2 \, dz$',
    r'Вычислить интеграл, используя формулу Коши-Грина: $\displaystyle\oint\limits_{max(|x|),|y|)=2} \overline{z}e^z \, dz$',
    r'Вычислить интеграл, используя формулу Коши-Грина: $\displaystyle\oint\limits_{max(|x|),4|y|)=1} \overline{z}^2z^3 \, dz$',
    r'Вычислить интеграл, используя формулу Коши-Грина: $\displaystyle\oint\limits_{max(|x|),3|y|)=3} \overline{z}\sin{\overline{z}} \, dz$'
]
ALL_TASKS = (TASKS1, TASKS2, TASKS3, TASKS4, TASKS5, TASKS6)