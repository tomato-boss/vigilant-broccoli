Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import telebot
import random

TOKEN = '6560704217:AAGDligvi7dhFCP3opUY-dBPxyAUEo9poHg'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Список предсказаний
predictions = [
    "Ведите обычную жизнь необычным способом.",
    "Не ищите внешних врагов: чтобы понять, что мешает Вашему развитию, загляните внутрь себя.",
    "Помните, что истинное партнерство может существовать только между цельными личностями.",
    "Будьте внимательны к подсказкам судьбы.",
    "Если колодец засорен, то самое время его очистить.",
    "Выигрыш исходит от того, с чем Вы должны расстаться.",
    "Действуйте в соответствии не со старыми авторитетами, а с тем, что Вы считаете правильным для Вас.",
    "Пришло время закончить старое и начать новое.",
    "Если не хотите серьезных потрясений, проанализируйте Ваше отношение к собственной личности.",
...     "Отпустите свое прошлое: оно исчерпало себя.",
...     "Не ожидайте слишком многого и не думайте о конечном результате.",
...     "Изучайте Ваши теневые стороны; поймите, что притягивает в Вашу жизнь несчастья.",
...     "Завершите то, что начали.",
...     "Будьте терпеливы, и если решение Ваше правильно, Вселенная поддержит его.",
...     "Не поддавайтесь эмоциям.",
...     "Присмотритесь к своему здоровью.",
...     "Наслаждайтесь удачей и делитесь ею с окружающими Вас людьми.",
...     "Сосредоточьтесь на настоящем.",
...     "Не ждите быстрых результатов.",
...     "Смиритесь: Ваши возможности ограничены.",
...     "Будьте настойчивы в битве с собственным эгоизмом.",
...     "Ваша энергия утекает из-за необдуманного или несвоевременного действия.",
...     "Плывите по течению жизни без оценок и попыток понять ее.",
...     "Не переоценивайте свои силы: это может привести к перенапряжению.",
...     "События полностью вне Вашего контроля.",
...     "Доверяйте тому, что с Вами происходит.",
...     "Размышляйте и не спешите с действиями.",
...     "Пришло время действовать, даже если от Вас требуется прыгнуть в пустоту.",
...     "Не пытайтесь упрямо проявлять свою ВОЛЮ.",
...     "Раскройтесь и пропустите свет в ту часть своей жизни, которая до сих пор была тайной."
... ]
... 
... # Обработчик команды '/start'
... @bot.message_handler(commands=['start'])
... def send_welcome(message):
...     bot.reply_to(message, "Привет! Я бот с предсказаниями. Напиши /predict, чтобы получить свое предсказание.")
... 
... # Обработчик команды '/predict'
... @bot.message_handler(commands=['predict'])
... def send_prediction(message):
...     prediction = random.choice(predictions)
...     bot.reply_to(message, prediction)
... 
... # Запуск бота
... bot.polling(none_stop=True)
