# Django_shop

Web application created based on the Django framework in Python. The application was designed for simplicity of use, intuitive interface and effective management of store content.


## 💡 Technologies:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)	![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
	![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
## 💭 Main features:

* Registration as a seller or regular user,
* Login and logout,
* Adding products to the cart,
* Editing and deleting the contents of the cart,
* Placing an order by completing the form,
* Finalize your order by updating your payment status,
* Ability to add, edit and delete product ratings after placing an order,

##### In the profile of logged:
 * It has the ability to update data,
 * Has access to orders,
 * Has access to submitted opinions,

##### Additional features for logged in sellers:
 * Ability to add, edit and remove products,
 * Information about products sold,
 * Browsing the products listed for sale,

##### Celery:
 * Asynchronous generation of order reports,
 * Downloading reports to your desktop in pdf or xlsx format,
 * Sentry - logging, monitoring errors and information about the task progress.

##### REST Framework:
* Unlogged in users can view a list of products and a detail product,
* Login and display the token,
* Authenticated users using the token can view product reviews, average product rating, list of ordered items, generate a new report, display and download (PDF/XLXS),
* Authenticated sellers can view the list of products sold, current products for sale, create, edit and delete products,
* Swagger/OpenAPI Documentation Generator for Django REST Framework,

## ⌛Status:
The project is in its final phase. Application tests will be added soon.


## 💿 Installation:

1. Clone Repository & Install Packages.

```bash
git clone https://github.com/wiktoriamarszewska77/Django_shop.git
pip install -r requirements.txt
```
2. Setup Virtualenv.
```bash
virtualenv env
source env/bin/activate
```
3. Launching the application by launching the container.
```bash
docker-compose up --build
```

## 🙋‍♂️ Contact:

e-mail [wiktoria.marszewska@wp.pl](wiktoria.marszewska@wp.pl)
