# 🛒 Django Marketplace Platform

## 📦 Overview
This project is a full-featured **e-commerce marketplace** built with **Django** on the backend and **vanilla HTML, CSS, and JavaScript** on the frontend. 

Every user can act as both a **buyer** and a **seller**, creating a dynamic and flexible platform for online commerce.

---

## 🔑 Key Features

### 👤 User Profile
- Unified user roles: all users can list products and make purchases.
- Profile page to view personal details, listed products, order history, and wallet balance.

### 🛍️ Product Listings
- Browse all available products posted by other users.
- Filter and sort functionality (e.g., price, category, date posted).

### ➕ Product Posting
- Authenticated users can post products with:
  - Title
  - Description
  - Price
  - Image upload
  - Stock availability

### 🛒 Add to Cart
- Add products to your shopping cart.
- Quantity management and subtotal calculation.

### 📦 Orders
- Place orders from your cart.
- View all your order history including status and total spent.

### 💰 My Wallet
- View wallet balance.
- Automatic deductions on purchases.
- Earnings from sold products reflected in the wallet.

---

## ⚙️ Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Backend      | Django (Python)           |
| Frontend     | HTML, CSS, JavaScript     |
| Database     | SQLite (default), easily replaceable with PostgreSQL/MySQL |
| Templates    | Django Templating Engine  |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/marketplace-platform.git
cd marketplace-platform
