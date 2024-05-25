# CoinTap Backend

CoinTap Backend is the server-side component of the CoinTap application. It provides APIs to interact with the frontend application, manage user scores, and handle authentication. This documentation will guide you through the setup, usage, and endpoints of the CoinTap Backend.



## Prerequisites

- Node.js (v12 or higher)
- npm (v6 or higher)
- PostgreSQL database
- Git


## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/cointap-backend.git
   cd cointap-backend
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Database Configuration**
   - Create a PostgreSQL database.
   - Update the database configuration in `.env` file.

4. **Run Migrations**
   ```bash
   npm run migrate
   ```

5. **Start the Server**
   ```bash
   npm start
   ```

The backend server should now be running at `http://localhost:3001`.


## API Endpoints

### Fetch User Data

**Endpoint:**
```http
GET /api/user?username={username}
```

**Response:**
```json
{
  "username": "fyzanshaik",
  "score": 100
}
```

### Update User Score

**Endpoint:**
```http
POST /api/user
```

**Request Body:**
```json
{
  "username": "fyzanshaik",
  "score": 150
}
```

**Response:**
```json
{
  "success": true
}
```

## Database Schema

### user_scores Table

- `id`: Primary key (integer)
- `username`: User's username (string)
- `score`: User's score (integer)

## Deployment

### Deploying to Heroku

1. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

2. **Set Environment Variables**
   ```bash
   heroku config:set DATABASE_URL=your-database-url
   ```

3. **Deploy to Heroku**
   ```bash
   git push heroku main
   ```

4. **Run Migrations**
   ```bash
   heroku run npm run migrate
   ```

The backend should now be deployed and accessible via the provided Heroku URL.

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure the database URL is correctly configured.
   - Check the database credentials and connectivity.

2. **Migrations not Running**
   - Verify the database configuration in the `.env` file.
   - Ensure the database is accessible from the application.

3. **Endpoint Errors**
   - Check the request format and ensure it matches the API documentation.
   - Verify the server logs for any error messages.

## Contribution

We welcome contributions! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

