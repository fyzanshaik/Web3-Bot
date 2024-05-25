# CoinTap Application

CoinTap is a web application that allows users to earn virtual coins by tapping a button. The application integrates with a backend to fetch and save user scores. This documentation will guide you through the setup, usage, and components of the CoinTap app.


## Prerequisites

- Node.js (v12 or higher)
- npm (v6 or higher)
- Git

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/cointap.git
   cd cointap
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Environment Variables**
   Create a `.env` file in the root directory and add the following:
   ```env
   REACT_APP_BACKEND_URL=https://your-backend-url.com
   ```

4. **Start the Application**
   ```bash
   npm start
   ```

The application should now be running at `http://localhost:5173`.

## Usage

1. **Access the Application**
   Open your browser and navigate to `http://localhost:3000`.

2. **Tapping to Earn Coins**
   - Tap the coin button to earn coins.
   - The current score is updated with each tap.
   - The wallet balance is fetched from the backend every 10 seconds.

3. **User Feedback**
   - Alerts are shown if you tap too fast or exceed the tap limit.

## Components

### CoinTap.tsx

The main component of the application that handles user interactions and displays the current score.

**Props:**
- `username`: The username of the current user.
- `initialScore`: The initial score fetched from the backend.
- `currentScore`: The current score after tapping.

### WalletBalance

A component that displays the user's wallet balance.

**Props:**
- `balance`: The current balance of the user's wallet.

### useFetchUserData

A custom hook to fetch user data from the backend.

**Usage:**
```typescript
const { score, setScore } = useFetchUserData(username);
```

### useSaveScore

A custom hook to save the user's score to the backend at regular intervals.

**Usage:**
```typescript
useSaveScore(initialScore, currentScore, username);
```

### useTapHandler

A custom hook to handle tap events and update the score.

**Usage:**
```typescript
const { score, handleTap } = useTapHandler(currentScore, 5000, 100);
```

## API Integration

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

### Save User Score

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

## Deployment

### Deploying Frontend

1. **Build the Application**
   ```bash
   npm run build
   ```

2. **Deploy to Vercel**
   ```bash
   npm install -g vercel
   vercel
   ```

## Troubleshooting

### Common Issues

1. **Application not starting**
   - Ensure all dependencies are installed.
   - Check the `.env` file for correct environment variables.

2. **API requests failing**
   - Ensure the backend is running and accessible.
   - Verify the `REACT_APP_BACKEND_URL` in the `.env` file.

3. **CORS Issues**
   - Ensure CORS is properly configured on the backend.

## Contribution

We welcome contributions! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.