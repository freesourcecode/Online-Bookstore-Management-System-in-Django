# Online Bookstore Management System in Django with Source Code

This **Online Bookstore Management System Project in Django** created based on **Python**, **Django**, and **SQLITE3 Database**.

The **Online Book Store System** is a simple project that can assist book store businesses in providing their customers with a simple way to conduct online transactions.

The system organizes all of the store’s books by book categories and stores all of the store’s books for sale information.

The book can be classified into different categories in this scheme, and it will appear when a customer searches for a specific category on the website or in an online store.

This system is a basic e-commerce platform with an admin side where the shop staff or admin can handle data and, most importantly, the books they sell in their store.

A Online Bookstore Management System Before making any transaction with the system, the store customer must first register on the website.

This device, like every other e-commerce platform, allows customers of the book store to temporarily store their chosen book or products in a cart for later checkout.

Since the system accept online payments, all transactions will be done via pay pal and credit card.

This Online Bookstore System in Django is an easy project for beginners to learn how to build a web-based python Django project.

>[!NOTE]
> To start creating an **Online Bookstore Management System in Python Django**, makes sure that you have PyCharm Professional IDE Installed in your computer.

## Admin Features

* **Dashboard**

For the admin dashboard, you will be able to all the basic access in the whole system. Such as summary of products, orders, and the categories.

* **Manage Books**

The admin has access to the books management information system. He can add, update and delete the books.

* **Manage Categories**

The page where the admin can add, edit and delete categories information.

* **Manage Orders**

As the main functions of the admin, the admin can accept or reject the order from the customers on a case to case basis and the list of customer orders are listed.

* **Manage User**

The admin can manage the user’s account. Admin can add, update and Block user in the system.

* **Login and Logout**

By default one of the security features of this system is the secure login and logout system.


## Customer Features

* **Login Page**

Customer enter their website credentials on this page to gain access in order to log in.

* **Register Page**

The page where new customer created their login credentials for the website.

* **Home Page**

When customer visit the website, this is the system’s default page. This page shows the books for sale in the store, or by entering a keyword in the search box above the books.

* **Book View Page**

The page on which the product’s specific information is shown, as well as the page on which the customer adds the product to his or her cart.

*  **Cart List Page**

The page that lists the items that customer have chosen. This is the page where the customer can complete the order checkout process.

* **My Order Page**

The page that lists the customer’s orders.

*  **Paypal and Credit Card Payments**

This Online Bookstore System in Django has a payment method that uses Paypal and Credit Card Payments.

## How to Create an Online Bookstore System in Django?

Here are the steps on how to create an **Online Bookstore System in Django** with Source Code.

1. **Open file.**
First, open “pycharm professional” after that click “file” and click “new project”.

![image](https://github.com/user-attachments/assets/33052da9-ebc3-4282-96ab-7cb0455dac7b)

2. **Choose Django.**

Next, after click “new project”, choose “Django” and click.

![image](https://github.com/user-attachments/assets/3be717de-8237-4c8f-8c76-ece946e86de6)

3. **Select file location**.

Then, select a file location wherever you want.

4. **Create application name**.

After that, name your application.

5. **Click create.**

Lastly, finish creating project by clicking “create” button.

6. **Start Coding.**

Finally, we will now start adding functionality to our Django Framework by adding some functional codes.

## Functionality and Codes

* **Create template for the category page**

In this section, we will learn on how create a templates for the category page. 

To start with, add the following code in your category.html under the folder of store/templates/store.

```
{% extends 'store/base.html' %}
{% load customfunction %}
{% block container %}
			<div class="row">
				{% for item in book %}
				<div class = 'col-sm-3'>
					<div class="book-wrapper text-center">
						<div class="coverpage">
							<img src="{{ item.coverpage.url }}"/>
						</div>
						<a href="{% url 'store:book' id=item.id %}">{{ item.name }}</a>
						<a href="{% url 'store:writer'  id=item.writer.id %}">{{ item.writer }}</a>
						<div class="rating">
							{{ item.totalrating|averagerating:item.totalreview }}
							<span class="totalrating">{{ item.totalreview|add:-1 }}</span>
						</div>
						<p> ₱{{ item.price }}</p>
						<button class="btn btn-danger" id="addTocart" data-book-id="{{ item.id }}">
								<i class="fa fa-shopping-cart""></i>Add to cart
						</button>
					</div>
				</div>
				{% endfor %}

			</div>
			{% if book|length > 0 %}
			<div class="d-pagination">
			    <ul class="pagination">
				{% if book.has_previous %}
					<li class="page-item">
						<a class="page-link" href="?page=1">First</a>
					</li>								
					<li class="page-item">
						<a class="page-link" href="?page={{ book.previous_page_number }}">Previous</a>
					</li>
				{% endif %}
				{% for ord in book.paginator.page_range %}
					{% if book.number == ord %}
						<li class="page-item active">
							<span class="page-link">{{ ord }}
								<span class="sr-only">(current)</span>
							</span>
						</li>
					{% elif ord > book.number|add:'-3' and ord < book.number|add:'3' %}
						<li class="page-item">
							<a class="page-link" href="?page={{ ord }}">{{ ord }}</a>
						</li>

					{% endif %}

				{% endfor %}
				 {% if book.has_next %}
					<li class="page-item">
						<a class="page-link" href="?page={{ book.next_page_number }}">Next</a>
					</li>
					<li class="page-item">
						<a class="page-link" href="?page={{ book.paginator.num_pages }}">Last</a>
					</li>
				{% endif %}
			    </ul>
			</div>
			{% else %}
			<h3 class="text-center mt-5">There are no books Found.</h3>
			{% endif %}	

{% endblock %}
```
* **Create template for the cart**

In this section, we will learn on how create a templates for the cart.

To start with, add the following code in your cart.html under the folder of cart/templates/cart.

```
{% extends 'store/base.html' %}

			{% block container %}
			<div class="row">
				<div class="col-sm-8">
					<div class="cart_info">
					    <table class="table table-hover">
					        <thead class="text-center">
					            <tr>
					                <th scope="col">#</th>
					                <th scope="col" style="width: 250px">Name</th>
					                <th scope="col" style="width: 250">Qty</th>
					                <th scope="col">Price</th>
					                <th scope="col">Action</th>
					            </tr>
					        </thead>
					        <tbody class="text-center">
					        {% for item in cart %}
					        	{% with book=item.book %}
				           		 <tr>
					                <td class="cart_coverpage"><a href=""><img src="{{ book.coverpage.url }}"></a></td>
					                <td>{{ book.name }}</td>
					                <td class="cart_quantity"><input type="text" name="qty" value="{{ item.quantity }}" onchange ="updateCartItem(this,{{ book.id }})" style="width: 30px"></td>
					                <td id="{{ book.id }}">₱{{ item.total_price }}</td>
					                <td><a href="{% url 'cart:cart_remove' bookid=book.id %}" class="btn btn-danger"><i class="fa fa-trash-o"></i></a></td>
					            </tr>
					            {% endwith %}
					        {% endfor %}
					        </tbody>
					    </table>
						<div class="continue_or_next text-center">
							<a href="{% url 'store:index' %}" class="btn btn-danger _to_shope ">Continue Shopping</a>
							<a href="{% url 'order:order_create' %}" class="btn btn-primary _to_continue">Proceed to Checkout</a>
						</div>
					</div>
				</div>
				<div class="col-sm-4" id="abc">

				</div>
			</div> 
			{% endblock %}


{% block scripts %}
	<script type="text/javascript">

	$(document).ready(function(){
		summary();
 
	}); 
	function summary(){
		$.ajax({
			url : "summary",
			type : "GET",
			success : function(data){
				$("#abc").html(data);
			}
		})
	}
	function updateCartItem(obj,id){
		$.ajax({
			url: "update/"+id+"/"+obj.value,
			type: "GET",
			data: {
				bookid: id,
				quantity: obj.value
			},
			success	:function(data){
				$("#"+(id.toString())).html(data);
				summary();
				totalCart();
			}
		})
	}

	</script>
{% endblock %}
```


### 📌Here's the full documentation for the [Online Bookstore Management System in Django](https://itsourcecode.com/free-projects/python-projects/online-bookstore-management-system-in-django-with-source-code/)
