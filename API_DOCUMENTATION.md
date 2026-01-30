# 📚 API Documentation - E-commerce Backend

## 🔐 Authentication & Users (`/api/auth/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| Register | POST | `/api/auth/register/` | No | Register new user |
| Login | POST | `/api/auth/login/` | No | Login and get JWT tokens |
| Refresh Token | POST | `/api/auth/refresh/` | Yes | Refresh access token |
| My Profile | GET | `/api/auth/profile/` | Yes | Get current user profile |
| Update Profile | PUT | `/api/auth/profile/` | Yes | Update current user profile |
| List Users | GET | `/api/auth/users/` | Admin | List all users |
| Block/Unblock User | PATCH | `/api/auth/users/<id>/block/` | Admin | Block or unblock user |

**Total: 7 APIs**

---

## 📦 Products & Categories (`/api/`)

### Categories

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| List Categories | GET | `/api/categories/` | No | List all categories |
| Create Category | POST | `/api/categories/` | Admin | Create new category |
| Update Category | PUT | `/api/categories/<id>/` | Admin | Update category |
| Delete Category | DELETE | `/api/categories/<id>/` | Admin | Delete category |

### Products

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| List Products | GET | `/api/products/` | No | List all products |
| Product Details | GET | `/api/products/<id>/details/` | No | Get product details |
| Create Product | POST | `/api/products/` | Admin | Create new product |
| Update Product | PUT | `/api/products/<id>/` | Admin | Update product |
| Delete Product | DELETE | `/api/products/<id>/` | Admin | Delete product |

**Total: 9 APIs**

---

## 🛒 Cart (`/api/cart/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| View Cart | GET | `/api/cart/` | Yes | Get user's cart |
| Add to Cart | POST | `/api/cart/add/` | Yes | Add product to cart |
| Update Quantity | PATCH | `/api/cart/items/<id>/` | Yes | Update item quantity |
| Remove Item | DELETE | `/api/cart/items/<id>/remove/` | Yes | Remove item from cart |
| Clear Cart | DELETE | `/api/cart/clear/` | Yes | Clear all items from cart |

**Total: 5 APIs**

---

## ❤️ Wishlist (`/api/wishlist/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| View Wishlist | GET | `/api/wishlist/` | Yes | Get user's wishlist |
| Add to Wishlist | POST | `/api/wishlist/add/` | Yes | Add product to wishlist |
| Remove Item | DELETE | `/api/wishlist/<id>/remove/` | Yes | Remove item from wishlist |

**Total: 3 APIs**

---

## ⭐ Reviews (`/api/reviews/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| Product Reviews | GET | `/api/reviews/products/<id>/` | No | Get reviews for a product |
| Add Review | POST | `/api/reviews/add/` | Yes | Add review to product |
| Update Review | PUT | `/api/reviews/<id>/` | Yes | Update own review |
| Delete Review | DELETE | `/api/reviews/<id>/delete/` | Yes | Delete own review |

**Total: 4 APIs**

---

## 🎟️ Coupons (`/api/coupons/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| Apply Coupon | POST | `/api/coupons/apply/` | Yes | Apply coupon code |
| Validate Coupon | POST | `/api/coupons/validate/` | No | Validate coupon code |
| Create Coupon | POST | `/api/coupons/create/` | Admin | Create new coupon |
| List Coupons | GET | `/api/coupons/list/` | Admin | List all coupons |
| Disable Coupon | PATCH | `/api/coupons/<id>/disable/` | Admin | Disable coupon |

**Total: 5 APIs**

---

## 🧾 Orders (`/api/orders/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| Create Order | POST | `/api/orders/create/` | Yes | Create order from cart |
| My Orders | GET | `/api/orders/my-orders/` | Yes | Get user's orders |
| Order Details | GET | `/api/orders/<id>/` | Yes | Get order details |
| All Orders | GET | `/api/orders/all/` | Admin | Get all orders |
| Update Order Status | PATCH | `/api/orders/<id>/status/` | Admin | Update order status |

**Total: 5 APIs**

---

## 💳 Payments (`/api/payments/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| Virtual Payment | POST | `/api/payments/pay/` | Yes | Process virtual payment |
| Payment Status | GET | `/api/payments/status/<order_id>/` | Yes | Get payment status |

**Total: 2 APIs**

---

## 🧑‍💼 Admin / CMS (`/api/admin/`)

| API | Method | Endpoint | Auth | Description |
|-----|--------|----------|------|-------------|
| Dashboard Stats | GET | `/api/admin/dashboard/stats/` | Admin | Get dashboard statistics |
| Sales Report | GET | `/api/admin/dashboard/sales-report/` | Admin | Get sales report |
| Product Stock Report | GET | `/api/admin/dashboard/stock-report/` | Admin | Get stock report |

**Total: 3 APIs**

---

## 🎯 Summary

| Module | APIs |
|--------|------|
| Auth & Users | 7 |
| Products & Categories | 9 |
| Cart | 5 |
| Wishlist | 3 |
| Reviews | 4 |
| Coupons | 5 |
| Orders | 5 |
| Payments | 2 |
| Admin | 3 |
| **Total** | **43** |

---

## 🔑 Authentication

All protected endpoints require JWT authentication. Include the token in the header:

```
Authorization: Bearer <access_token>
```

### Getting Tokens

1. **Register**: `POST /api/auth/register/`
   ```json
   {
     "username": "user123",
     "email": "user@example.com",
     "password": "password123",
     "password2": "password123"
   }
   ```

2. **Login**: `POST /api/auth/login/`
   ```json
   {
     "username": "user123",
     "password": "password123"
   }
   ```

Response includes:
```json
{
  "user": {...},
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

## 📝 Example Requests

### Create Order with Coupon
```bash
POST /api/orders/create/
Authorization: Bearer <token>
Content-Type: application/json

{
  "coupon_code": "SAVE20"
}
```

### Virtual Payment
```bash
POST /api/payments/pay/
Authorization: Bearer <token>
Content-Type: application/json

{
  "order_id": 1,
  "method": "virtual_card"
}
```

---

## 🚀 Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Run server:
   ```bash
   python manage.py runserver
   ```

5. Access APIs at: `http://localhost:8000/api/`

---

## 📌 Notes

- All prices are in Decimal format (2 decimal places)
- All dates are in ISO 8601 format
- Pagination is enabled (20 items per page)
- Virtual Payment always succeeds (for demo purposes)
- Coupon validation checks: active status, date range, usage limit

