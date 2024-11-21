import axios from 'axios';

const API_URL = 'http://localhost:8000/api/token/';

// Function to log in and obtain JWT tokens
export const login = async (username, password) => {
    try {
        const response = await axios.post(API_URL, {
            username,
            password,
        });
        if (response.data.access) {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
        }
        return response.data;
    } catch (error) {
        console.error('Login failed:', error);
        throw error;
    }
};

// Function to get the access token from local storage
export const getAccessToken = () => {
    return localStorage.getItem('access_token');
};
