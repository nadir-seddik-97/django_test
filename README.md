# Django Views Documentation

This documentation provides details about different views used in the Django project.

---
## Register View

### Description
The Register View enables users to create an account on the platform.

### Usage

**URL:** `/register/`

**Method:** `POST`

**Parameters:**
- `username`: User's username.
- `first name`: User's first name.
- `last name`: User's last name.
- `email`: User's email.
- `password`: User's password.
- `address`: User's address.
- `phone`: User's phone.
- `photo`: User's photo.

## Login View

### Description
The Login View enables users to Connect to their account on the platform.

### Usage

**URL:** `/`

**Method:** `POST`

**Parameters:**
- `username`: User's username.
- `password`: User's password.



# Add Order View

This view allows authenticated users to create an order by selecting products and quantities.

---

## Usage

### URL
`/add_order/`

### Method
`POST`

### Parameters
- `quantities`: JSON string containing selected products and quantities.

### Description

This view performs the following operations:

1. Verifies if the user is authenticated.
2. Accepts a POST request with the selected products and quantities.
3. Validates the form data and checks for selected products.
4. Creates an order instance with the selected products and calculates the total amount.
5. Redirects to the home page on successful order creation or back to the `add_order` page if no products are selected.



## Update Order View

### Method
- **POST**

### URL
- **`/update_order/<int:pk>/`**

### Parameters
- `pk`: ID of the order to be updated (integer)
- `new_products`: List containing selected new products.
- `new_quantities`: List containing selected new quantities.

### Description
This view updates an existing order by performing the following operations:

1. Verifies if the user is authenticated.
2. Fetches the existing order to update.
3. Checks if the logged-in user is the owner of the order.
4. Accepts a POST request to update the order details, including quantities for existing items and adding new items with quantities.
5. Calculates and updates the total amount for the order.
6. Redirects to the home page after successfully updating the order.


