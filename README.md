# Shared-Wishlist-App
Here’s your full `README.md` file content (excluding screenshots and license), ready to copy and place into your project root:

---

### ✅ `README.md`

```markdown
# 📝 Shared Wishlist App

A collaborative wishlist application where users can log in using Google, create wishlists, add products, and share their lists. Built with **Vue.js** (frontend) and **Flask** (backend).

---

##  Features

- ✅ **Google Sign-In** authentication via Firebase  
- ✅ **Create, View & Manage Wishlists**  
- ✅ **Add Products** (name, price, image)  
- ✅ **Responsive UI** with clean styling  
- ✅ **Separate views for wishlists and products**  
- ✅ **Back to Wishlist** navigation  
- ✅ Built for collaboration and sharing  

---

## 🛠️ Technologies Used

### Frontend
- Vue.js 3
- CSS / Flexbox / Grid
- Firebase (Google Auth)

### Backend
- Python Flask
- PostgreSQL
- REST API structure

---

## Project Structure

```

shared-wishlist-app/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── CreateWishlist.vue
│   │   │   ├── WishlistList.vue
│   │   │   └── WishlistDetail.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── public/
│   └── firebase.js
├── README.md
└── .gitignore

````

---

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/yashsonawane14/Shared-Wishlist-App.git
cd Shared-Wishlist-App
````

---

### 2. Setup Flask Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

* Flask backend runs at: `http://localhost:5000`

---

### 🌐 3. Setup Vue Frontend

```bash
cd frontend
npm install
npm run dev
```

* Vue app runs at: `http://localhost:5173`

---

## 🔐 Firebase Setup (Google Sign-In)

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Create a new project
3. Enable **Google Sign-In** under **Authentication**
4. Add your web app and copy the config
5. Paste config in `frontend/src/firebase.js`:

```js
const firebaseConfig = {
  apiKey: "...",
  authDomain: "...",
  projectId: "...",
  appId: "..."
};
```

---

##  How It Works

* Users **log in with Google**
* They can **create wishlists**
* Each wishlist supports **adding products** (with image, price, name)
* Flask backend stores and serves data via REST APIs
* Vue frontend interacts with backend using fetch API
* **Back to wishlists** navigation allows seamless movement

---

## API Endpoints (Flask)

| Endpoint                      | Method | Description                  |
| ----------------------------- | ------ | ---------------------------- |
| `/api/wishlists/<user_id>`    | GET    | Get all wishlists of a user  |
| `/api/wishlists/`             | POST   | Create new wishlist          |
| `/api/products/<wishlist_id>` | GET    | Get all products in wishlist |
| `/api/products/`              | POST   | Add product to wishlist      |


