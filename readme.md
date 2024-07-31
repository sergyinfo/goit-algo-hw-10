# Висновки

Проект демонструє застосування методу Монте-Карло для обчислення інтегралу функції \( f(x) = x^2 \) на інтервалі від 0 до 2. Використання 10,000 випадкових точок дало приблизне значення інтегралу 2.648.

## Точність методу Монте-Карло

- **Обчислене значення:** 2.648
- **Точне значення інтегралу (за допомогою SciPy `quad`):** 2.667
- **Абсолютна помилка:** \( 2.96 \times 10^{-14} \)

Ці результати підтверджують, що метод Монте-Карло може бути ефективним для апроксимації інтегралів, особливо коли аналітичне обчислення є складним або неможливим. Хоча метод і має певну похибку порівняно з аналітичними методами, його простота і універсальність роблять його корисним інструментом у чисельних методах.

## Візуалізація результатів

Графічне представлення включає криву функції \( f(x) = x^2 \), зону під кривою, яка інтегрується, а також точки, що використовувались у методі Монте-Карло. Це дозволяє візуально оцінити, як точки розподілені відносно кривої, і наглядно продемонструвати, як метод апроксимує область під кривою.

