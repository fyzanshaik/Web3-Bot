# CoinTap Full Stack Application

CoinTap is a full stack web application that allows users to earn virtual coins by tapping a button. The application consists of a frontend, a backend, and a Telegram bot for additional user interaction.

## Table of Contents
- [Project Structure](#project-structure)
- [Folders Overview](#folders-overview)
  - [backend](#backend)
  - [frontend](#frontend)
  - [telegram-bot](#telegram-bot)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [License](#license)

## Project Structure

```
coin-game/
├── backend/
├── frontend/
└── telegram-bot/
```

## Folders Overview

### `backend`

This folder contains the server-side code for the CoinTap application. It includes the following key files:

- **server.ts**: Entry point for the Express server.
- **database.ts**: Database configuration and connection.
- **controllers/**: Contains the controller logic for handling API requests.
  - **userController.ts**: Handles fetching and updating user data.
- **routes/**: Defines the API routes.
  - **userRoutes.ts**: Routes for user-related operations.

### `frontend`

This folder contains the client-side code for the CoinTap application. It includes the following key files:

- **src/**
  - **components/**: React components used in the application.
    - **CoinTap.tsx**: Main component for the coin tapping functionality.
  - **hooks/**: Custom hooks for data fetching and state management.
    - **useFetchUserData.ts**: Hook to fetch user data from the backend.
    - **useSaveScore.ts**: Hook to save the score to the backend.
    - **useTapHandler.ts**: Hook to handle the tap logic.
  - **App.tsx**: Main application component.
  - **index.tsx**: Entry point for the React application.

### `telegram-bot`

This folder contains the code for the Telegram bot integration. It includes the following key file:

- **bot.py**: Main bot logic and command handling.
  - **start**: Command handler to start the bot and greet users.
  - **handle_message**: Handler to process admin messages and send them to a specified channel.
  
  The bot uses environment variables for configuration:
  - `BOT_TOKEN`: The bot's token.
  - `ADMIN_USERNAME`: The Telegram username of the bot's administrator.
  - `CHANNEL_ID`: The ID of the channel where announcements will be sent.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.