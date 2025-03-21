Here's a sample `README.md` file for your AI-powered resume screening app with UI:

```markdown
# AI-Powered Resume Screening App

This project is an AI-powered resume screening application that provides a user-friendly interface (UI) for screening resumes using an AI model. The app is split into two main components:

1. **UI (Frontend)**: Provides a user interface for interacting with the resume screening tool.
2. **Backend**: Contains the AI-powered resume screening logic, wrapped in a Docker container.

## Project Structure

The project is divided into two main folders:

- `resume-screening-ui`: Contains the frontend/UI of the application.
- `resume-screening`: Contains the backend logic and a Dockerfile to build the application backend.

## Getting Started

### Prerequisites

- Node.js (for frontend)
- Docker (for backend)
- OpenAI API key (for backend integration)

### Step 1: Set Up the Frontend (UI)

1. Navigate to the `resume-screening-ui` folder:
   ```bash
   cd resume-screening-ui
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Start the UI server:
   ```bash
   npm run dev
   ```

   This will start the UI server, and you should be able to access the application on your browser (usually `http://localhost:5173`).

### Step 2: Set Up the Backend

1. Navigate to the `resume-screening` folder:
   ```bash
   cd resume-screening
   ```

2. Edit the `.env` file in the `resume-screening` folder:
   - Replace the placeholder value for the `OPENAI_API_KEY` with your own OpenAI API key. For example:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

3. Build the Docker container:
   ```bash
   docker build -t resume-screening .
   ```

4. After building the Docker image, you can run the container:
   ```bash
   docker run -d -p 8000:8000 resume-screening
   ```

   This will start the backend server, usually accessible at `http://localhost:5000`.

### Step 3: Testing the Application

- Once both the frontend and backend are up and running, the UI (frontend) will be able to interact with the backend.
- You can now upload resumes and have them screened by the AI model through the app.


## Notes

- Ensure that your OpenAI API key is kept secure and never exposed publicly.
- If you face issues with Docker or have any other problems, make sure Docker is installed and running on your machine.
- The backend is developed via FastAPI and will be accessible at `http://localhost:800/docs`.
- The frontend communicates with the backend at `http://localhost:5173`, so ensure the backend is running before interacting with the UI.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README.md` file includes instructions on how to set up both the frontend and backend components, as well as details on how the project is structured. Let me know if you'd like any adjustments!
