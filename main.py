from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

best_cafe = ['Чашка Espresso Bar (Большая Васильковская 1-3/2);',
             'Takava Coffe-Buffet (ул. Большая Васильковская, 1-3);',
             'Yellow place (ул. Мечникова, 9);',
             'Coffee in Action (сеть);',
             'Gemini Roastery (ул. Антоновича, 172);',
             'Blur Coffee (ул. Мечникова, 5);']

meat_restaurant = ['BEEF meat & wine (ул Шота Руставели, 11);',
                   'Argentina Grill (ул. Маршала Тимошенко, 18);',
                   'Grill do Brasil (бульвар Леси Украинки, 24);',
                   'В ребро (пр-кт Героев Сталинграда, 24А);',
                   "Sam's Steak House (ул. Жилянская, 37);"]

fish_restaurant = ['Odessa Restaurant (ул. Большая Васильковская, 114);',
                   'Рыба Пила (ул. Большая Васильковская, 112);',
                   "Egersund Seafood (пр-кт П. Григоренко, 32Д);",
                   "Рыбный Базар (ул. Владимирская, 24A);",
                   "Alaska (ул. Сечевых Стрельцов, 20);",
                   "Черноморка на Подоле (ул. Ярославская, 5/2);"]

ukraina_food = ['SHO (ул. Мечникова, 18А);',
                'КАНАПА ресторан. салон (Андреевский спуск, 19А);',
                'BARVY (ул. Мечникова, 3);',
                'Последняя Баррикада (ул. Майдан Незалежности, 1);']

national_food = ["Шоты (Мечникова, 9);",
                 "МАМА МАНАНА (ул. Большая Васильковская, 44)",
                 "17.804 Indonesian Social Kitchen (ул. Большая Васильковская, 82)",
                 "Himalaya Restaurant (ул. Большая Васильковская, 80);",
                 "Чичико (ул. Ярославов Вал, 23А);",
                 "Шотландский дом-ресторан Whisky Corner (Софиевская, 16);",
                 "Жасмин (пр-кт Валерия Лобановского, 118);"]

konditer = ["Milk Bar (ул. Шота Руставели, 16);",
            "The Cake (ул. Большая Васильковская, 5);",
            "Madame Josy (ул. Бориса Гринченко, 4);",
            "Bassano Dolceteka (ул. Большая Васильковская, 100);"]

wine = ["Vino e Cucina (Сечевых Стрельцов, 82);",
        "Osteria Pantagruel (ул. Лысенко, 1);",
        "Lucky Restaurant Vinoteque (ул. Мечникова, 9);",
        "Bassano Ristorante (ул. Большая Васильковская, 100);",
        "Veranda on the river (Набережное шоссе, 11А);"]

beer = ["Syndicate Beer & Grill (ул. Михаила Омельяновича-Павленко , 4/6);",
        "This is Пивбар (ул. Тростянецкая, 4/2);",
        "Пивная Дума (сеть);",
        "Brugge (ул. Маршала Конева, 8);",
        "Ресторан-пивоварня Cosmopolite (ул. В. Гетьмана, 6);"]

bar = ["LoggerHead (бульв. Тараса Шевченко, 1);",
       "БарменДиктат (ул. Крещатик, 44);",
       "Hendrick`s bar (ул. Богдана Хмельницкого, 42);",
       "Hangover (ул. Грушевского, 3А);",
       "Alchemist Bar (ул. Шота Руставели, 12);",
       "Pink Freud (ул. Нижний Вал, 19);",
       "N::B Cocktails Bar (ул. Михайловская, 13);"]




@app.route('/')
def index():
    head = "Лучшая кофейня"
    name = []
    address = []
    for x in best_cafe:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)

@app.route('/meat')
def meat():
    head = "Лучший мясной ресторан"
    name = []
    address = []
    for x in meat_restaurant:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)

@app.route('/fish')
def fish():
    head = "Лучший рыбный ресторан"
    name = []
    address = []
    for x in fish_restaurant:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)

@app.route('/ukraine')
def ukraine():
    head = "Лучший ресторан украинской кухни"
    name = []
    address = []
    for x in ukraina_food:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)

@app.route('/national')
def national():
    head = "Лучший ресторан национальной кухни"
    name = []
    address = []
    for x in national_food:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)

@app.route('/сonf')
def conf():
    head = "Лучшая кондитерская"
    name = []
    address = []
    for x in konditer:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)

@app.route('/wine')
def wine_():
    head = "Ресторан с лучшей винной картой"
    name = []
    address = []
    for x in wine:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)


@app.route('/beer')
def beer_():
    head = "Лучший пивной ресторан"
    name = []
    address = []
    for x in beer:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)

@app.route('/bar')
def bar_():
    head = "Лучший бар"
    name = []
    address = []
    for x in bar:
        name.append(x.split('(')[0])
        address.append(x.split('(')[1][:-2])
    return render_template('index.html', name=name, address=address, category=head)





app.run(debug=True)