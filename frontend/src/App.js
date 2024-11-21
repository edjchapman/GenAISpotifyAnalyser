import React, { useEffect, useState } from 'react';
import apiClient from './services/apiService';
import { login } from './services/authService';

const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Example login - you can replace with your login UI or existing logic
    const performLogin = async () => {
      try {
        await login('username', 'password'); // Replace with actual credentials
        fetchAnalysisData();
      } catch (error) {
        console.error('Failed to log in:', error);
      }
    };

    performLogin();
  }, []);

  const fetchAnalysisData = async () => {
    try {
      const response = await apiClient.get('analyze/');
      setData(response.data);
    } catch (error) {
      console.error('Error fetching analysis data:', error);
    }
  };

  if (!data) return <p>Loading...</p>;

  return (
      <div className="App">
        <h1>Spotify Analyzer</h1>
        <div>
          <h2>Top Genres</h2>
          <ul>
            {Object.entries(data.top_genres).map(([genre, count]) => (
                <li key={genre}>{genre}: {count}</li>
            ))}
          </ul>
        </div>
      </div>
  );
};

export default App;
