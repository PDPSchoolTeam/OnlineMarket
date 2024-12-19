## Online Shoppping Application
#### `1 . Main Page`
![img_5.png](img_5.png)
#### `2. Product Page`
![img_7.png](img_7.png)
#### `3. Cart Page`
![img_8.png](img_8.png)
#### `4. Orders Page`
![img_6.png](img_6.png)
#### `5. Favourite Page`
![img_9.png](img_9.png)

## Installation ans Set Up
<pre>git clone https://github.com/theMirmakhmudov/OnlineMarketApplication.git</pre>
<pre>pythom -m venv .venv</pre>
<pre>source .venv/bin/activate</pre>
<pre>pip install -r requirements.txt</pre>
<pre>cp .env-sample .env</pre>
### Migrations
<pre>python3 manage.py makemigrations</pre>
<pre>python3 manage.py migrate</pre>
<pre>python3 manage.py runserver</pre>

### Migrations with Make file
<pre>make make_mig</pre>
<pre>make mig</pre>
<pre>make run</pre>

### Create Super Admin

<pre>python3 manage.py createsuperuser</pre>

### Create Super Admin with Make file

<pre>make admin</pre>

<hr>

<footer>© Copyright 2024 Responsibility Team.</footer>